/*jslint browser:true */
/*globals $, self */


var TUTORONS_SERVER = 'http://127.0.0.1:8000';
var TUTORONS = ['wget', 'css'];

// Send a request to the server to have it process this page
var j;
for (j = 0; j < TUTORONS.length; j++) {
    $.post(TUTORONS_SERVER + '/' + TUTORONS[j], {
        'origin': window.location.href,
        'document': document.body.innerHTML,
    });
}



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


document.body.onmouseup = function() {

    var selection =  window.getSelection();
    var selString = selection.toString();
    if (selString.length > 0) {
        var msg = "";
        var range = selection.getRangeAt(0);
        var node = getEncapsulatingNode(range);
        var parents = [node].concat($(node).parents().toArray());
        var i, selector, par, offsets;
        for (i = 0; i < parents.length; i++) {
            par = parents[i];
            selector = getCssSelector(par);
            offsets = offsetsWithinElement(par, range);
            console.log('[' + offsets.start + ',' + offsets.end + '], ' + selector);
            msg += [selector, offsets.start, offsets.end].join('\t') + '\n';
        }
        self.port.emit('copy', {'msg': msg});
    }

};
