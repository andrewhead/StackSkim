var self = require('sdk/self');
var data = require('sdk/self').data;
var pageMod = require('sdk/page-mod');
var clipboard = require('sdk/clipboard');


pageMod.PageMod({
    include: '*',
    contentScriptFile: [
        data.url('jquery-2.1.3.min.js'),
        data.url('copy-selection.js'),
    ],
    attachTo: ['existing', 'top'],
    onAttach: function(worker) {
        worker.port.on('copy', function(payload) {
            clipboard.set(payload.msg);
        });
    },
});
