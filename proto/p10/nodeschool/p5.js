var fs = require('fs');
var path = require('path');

var pathname = process.argv[2];
var ext = process.argv[3];
var i, item;

fs.readdir(pathname, function(err, list) {
    for (i = 0; i < list.length; i++) {
        item = list[i];
        if (path.extname(item) === '.' + ext) {
            console.log(list[i]);
        }
    }
});
