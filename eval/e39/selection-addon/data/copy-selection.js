/*jslint browser:true */
/*globals $, self */


/* Find the first node that holds the full range */
function getEncapsulatingNode(range) {

    var sCont = range.startContainer;
    var eCont = range.endContainer;
    var startParents = [sCont].concat($(sCont).parents().toArray());
    var endParents = [eCont].concat($(eCont).parents().toArray());

    var i, j, sNode, eNode;
    for (i = 0; i < startParents.length; i++) {
        for (j = 0; j < endParents.length; j++) {
            sNode = startParents[i];
            eNode = endParents[j];
            if (sNode === eNode && sNode.nodeType === 1 && eNode.nodeType === 1) {
                return sNode;
            }
        }
    }

    return null;

}


/**
 * Get the CSS selector that points to a unique node.
 * REUSE: This method was modified from that at
 * http://stackoverflow.com/questions/4588119/get-elements-css-selector-without-element-id#4588211
 */
function getCssSelector(node) {
    var names = [];
    var c, e;
    while (node.parentNode){
        if (node === node.ownerDocument.documentElement) {
            names.unshift(node.tagName);
        }
        else {
            c = 1;
            e = node;
            while (e.previousElementSibling) {
                e = e.previousElementSibling;
                if (e.tagName === node.tagName) {
                    c++;
                }
            }
            names.unshift(node.tagName + ":nth-of-type(" + c + ")");
        }
        node = node.parentNode;
    }
    return names.join(" > ");
}


/**
 * Get offsets of a range within an element
 * REUSE: Based on code concept found at:
 * http://stackoverflow.com/questions/4811822/get-a-ranges-start-and-end-offsets-relative-to-its-parent-container#4812022
 */
function offsetsWithinElement(node, range) {

    var beforeRange, afterRange, nodeLength, sOffset, eOffset;

    beforeRange = range.cloneRange();
    beforeRange.selectNodeContents(node);
    beforeRange.setEnd(range.startContainer, range.startOffset);
    sOffset = beforeRange.toString().length;

    afterRange = range.cloneRange();
    afterRange.selectNodeContents(node);
    nodeLength = afterRange.toString().length;
    afterRange.setStart(range.endContainer, range.endOffset);
    eOffset = nodeLength - afterRange.toString().length;

    return {
        'start': sOffset,
        'end': eOffset,
    };

}


function getOffsetsInHtml(range) {
    var node = getEncapsulatingNode(range);
    var parents = $(node).parents().toArray();
    var i;
    for (i = 0; i < parents.length; i++) {
        if (parents[i].tagName === 'HTML') {
            return offsetsWithinElement(parents[i], range);
        }
    }
}


function prepTextForExcelEntry(text) {
    var textRevised = text;
    // Before we insert this into Excel, any leading double quotes and the next
    // double quotes they match need to be expanded to three quotation marks so
    // they are entered into the cell and not ignored.
    if (text.match(/^"/)) {
        var matches = 0;
        textRevised = text.replace(/"/g, function() {
            matches = matches + 1;
            if (matches <= 2) {
                return '"""';
            }
            return '"';
        });
    }
    return textRevised;
}


document.body.onmouseup = function() {

    var selection =  window.getSelection();
    var selString = selection.toString();
    if (selString.length > 0) {
        var msg = "";
        var range = selection.getRangeAt(0);
        var node = getEncapsulatingNode(range);
        var parents = [node].concat($(node).parents().toArray());
        var htmlOffsets = getOffsetsInHtml(range);
        var i, selector, par, offsets, start_char, end_char;
        for (i = 0; i < parents.length; i++) {
            par = parents[i];
            selector = getCssSelector(par);
            offsets = offsetsWithinElement(par, range);
            start_char = offsets.start;
            end_char = offsets.end - 1;  // ranges end at an index 1 after the last character
            msg += [
                start_char, 
                end_char,
                selector,
                // Together, the page URL together with the offsets of the 
                // text within the full body of the page should be a unique
                // identifier for this range
                window.location.href, 
                htmlOffsets.start,
                htmlOffsets.end,
                prepTextForExcelEntry(selString),
            ].join('\t') + '\n';
        }
        self.port.emit('copy', {'msg': msg});
    }

};
