var fs = require("fs");
var path = require('path');
var express = require('express');

var configFileName = "config.json";
var imageFileName = "sandbox.jpg";
var logFileName = "logs.txt";
var port = 3000;

var app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/logs', function(req, res) {
    fs.readFile(logFileName, (err, data) => {        
        if (err) 
        {
            console.error(err);
            res.end();
        }  
        res.send(data);
    }); 
});

app.get('/image', function(req, res){
    fs.readFile(imageFileName, (err, data) => {        
        if (err) 
        {
            console.error(err);
            res.end();
        }    
        res.send(data);
    }); 
});

app.get('/config', function(req, res) {
    fs.readFile(configFileName, (err, data) => {
        if (err) throw err;             
        res.json(JSON.parse(data));
    });    
});

app.post('/config', function(req, res){
    var json = JSON.stringify(req.body);
    fs.writeFile(configFileName, json, function (err) {
        if (err) throw err;         
        console.log('Data written successfully!', json);
        res.end();
    });
});

app.listen(port, function(){
    console.log('Listening on port ' + port);
})