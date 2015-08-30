var fs = require('fs');
var filename = process.argv[2];
var buffer = fs.readFileSync(filename);
var numLines = buffer.toString().split('\n').length;
console.log(numLines - 1);
