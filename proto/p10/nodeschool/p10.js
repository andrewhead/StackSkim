/*
 * p10.js
 * Copyright (C) 2015 andrew <andrew@C02MX11NFD58>
 *
 * Distributed under terms of the MIT license.
 */
var net = require('net');
var strftime = require('strftime');

var server = net.createServer(function (socket) {
    var msg = strftime("%Y-%m-%d %H:%M\n");
    socket.end(msg);
});
server.listen(process.argv[2]);
