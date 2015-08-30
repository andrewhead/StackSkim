var filename = process.argv[2];
var fs = require('fs');
fs.readFile(filename, function(err, data) {
    console.log(data.toString().split('\n').length - 1);
});
