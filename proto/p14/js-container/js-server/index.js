var http = require('http');
var request = require('request');


console.log("Building server");
var server = http.createServer(function (req, res) {
    console.log("Got request");
    res.writeHead(200, "text/plain");
    request('http://www.google.com', function (error, response, body) {
        if (!error && response.statusCode === 200) {
            res.end(body.substring(0, 100));
        }
        else {
            res.end("Failed to download site");
        }
    });
});

server.listen(8080);
