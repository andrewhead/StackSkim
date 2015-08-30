/*
 * p12.js
 * Copyright (C) 2015 andrew <andrew@C02MX11NFD58>
 *
 * Distributed under terms of the MIT license.
 */
var map = require('through2-map');
var http = require('http');

var server = http.createServer(function (req, res) {
    if (req.method !== "POST") {
        return res.end("Send me a POST\n");
    }
    req.pipe(map(function (chunk) {
        return chunk.toString().toUpperCase();
    })).pipe(res);
});
server.listen(process.argv[2]);
