var mod = require('./p6-module');

mod(process.argv[2], process.argv[3], function(err, data) {
    if (err !== null) {
        console.log("Error occurred!");
    } else {
        data.forEach(function(item) {
            console.log(item);
        });
    }
});
