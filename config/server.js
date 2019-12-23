var http = require('http');
var qs = require('querystring');
var fs = require("fs");
var configFileName = "config.json";

http.createServer(function (req, res) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Request-Method', '*');
    res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET, POST');
    res.setHeader('Access-Control-Allow-Headers', '*');
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }

    if (req.method == 'POST') {
        var body = '';

        req.on('data', function (data) {
            body += data;

            // Too much POST data, kill the connection!
            // 1e6 === 1 * Math.pow(10, 6) === 1 * 1000000 ~~~ 1MB
            if (body.length > 1e6)
                request.connection.destroy();
        });

        req.on('end', function () {
            var post = qs.parse(body);

            fs.writeFile(configFileName, post.data, function (err) {
                if (err) {
                    return console.error(err);
                }
                console.log("Data written successfully!", post.data);
            });

            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end();

        });
    }
    else {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end();
    }

    

}).listen(1337, "10.42.0.1");
