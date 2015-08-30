var bl = require('bl');
var http = require('http');

http.get(process.argv[2], function(response) {
    response.pipe(bl(function(err, data) {
        var message = data.toString();
        console.log(message.length);
        console.log(message);
    }));
});
