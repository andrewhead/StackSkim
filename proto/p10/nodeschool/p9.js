var http = require('http');
var bl = require('bl');
var results = [];
var urls = [process.argv[2], process.argv[3], process.argv[4]];
var completed = 0;


function onFinished(results) {
    results.sort(function (a, b) {
        return a.index - b.index;
    });
    results.forEach(function (res) {
        console.log(res.data);
    });
}

function submit (index, url, results) {
    http.get(url, function (response) {
        response.pipe(bl(function (err, data) {
            if (err) {
                return console.error(err);
            }
            results.push({
                'index': index,
                'data': data.toString()
            });
            if (results.length === urls.length) {
                onFinished(results);
            }
        }));
    });
}


urls.forEach(function (url, index) {
    submit(index, url, results);
});
