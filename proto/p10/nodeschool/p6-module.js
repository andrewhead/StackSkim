var fs = require('fs');
var path = require('path');

module.exports = function(pathname, ext, callback) {

    fs.readdir(pathname, function(err, list) {

        if (err)
          return callback(err);

        var validList = list.filter(function(item) {
            return path.extname(item) === '.' + ext;
        });

        return callback(null, validList);

    });

};
