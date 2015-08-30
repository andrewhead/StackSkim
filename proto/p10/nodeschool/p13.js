/*
 * p13.js
 * Copyright (C) 2015 andrew <andrew@C02MX11NFD58>
 *
 * Distributed under terms of the MIT license.
 */
var http = require('http');
var url = require('url');

var server = http.createServer(function (req, res) {

    var urlinfo = url.parse(req.url, true);
    var date = new Date(urlinfo.query.iso);
    var data;

    res.writeHead(200, {'Content-Type': 'application/json'});

    if (urlinfo.pathname === '/api/parsetime') {
        data = {
            'hour': date.getHours(),
            'minute': date.getMinutes(),
            'second': date.getSeconds()
        };
        console.log("Before return");
        return res.end(JSON.stringify(data) + '\n');
    }
    if (urlinfo.pathname === '/api/unixtime') {
        data = {
            'unixtime': date.getTime()
        };
        return res.end(JSON.stringify(data) + '\n');
    }

});

server.listen(process.argv[2]);
