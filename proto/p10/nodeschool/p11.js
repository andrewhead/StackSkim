/*
 * p11.js
 * Copyright (C) 2015 andrew <andrew@C02MX11NFD58>
 *
 * Distributed under terms of the MIT license.
 */
var fs = require('fs');
var http = require('http');

var server = http.createServer(function (request, response) {
    var fileStream = fs.createReadStream(process.argv[3]);
    fileStream.pipe(response);
});
server.listen(process.argv[2]);
