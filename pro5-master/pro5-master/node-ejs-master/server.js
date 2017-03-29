// load the things we need
var express = require('express');
var app = express();
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// connect to Mongo DB
mongoose.connect('localhost', 'pro3');

var A = mongoose.model('A', new Schema({
    depth : String,
    created : Date,
    site : String,
    description : String
}), 'sesmicinfo_quakedetail');

// set the view engine to ejs
app.set('view engine', 'ejs');
var http = require('http');
var options = {
    host : '127.0.0.1',
    port : '8000',
    path : '/disaster/'
};
var fs = require('fs');
var path = require('path');
var filePath = path.join(__dirname, 'activity.csv');
var data_mongo = [];

var watch = require('node-watch');

callback = function(response) {
	var str = '';

	// another chunk of data has been recieved, so append it to `str`
	response.on('data', function(chunk) {
		str += chunk;
	});

	// the whole response has been recieved, so we just print it out here
	response.on('end', function() {
		console.log(str);
	});
}

watch(filePath, function(req, res) {
	fs.readFile(filePath, function(err, data) {
		if (!err) {
			console.log('received data: ' + data);
			data_mongo = data.toString().split(",");
			console.log(data_mongo);
			var a = new A;
			a.depth = data_mongo[0];
			a.created = data_mongo[1];
			a.site = data_mongo[2];
			a.description = data_mongo[3];
			a.save(function(err, a) {
				if (err) throw err;
				console.error('saved img to mongo');
			});
		}
		else {
			console.log(err);
		}
		if (parseInt(data_mongo[3]) > 7) {
			http.request(options, callback).end();
		}
		app.render('pages/live', {
			dataR : data
		}, function(err, html) {
		});
	});

});

app.get('/', function(req, res) {
	fs.readFile(filePath, function(err, data) {
		if (!err) {
			console.log('received call from external server: ' + data);

		}
		else {
			console.log(err);
		}
		res.render('pages/index', {
			feed : data
		});
	});
});

app.get('/checkhealth', function(req, res) {
	res.header("Access-Control-Allow-Origin", "*");
	res.header("Access-Control-Allow-Headers",
	        "Origin, X-Requested-With, Content-Type, Accept");
	res.send({
	    "status" : "healthy",
	    "nodeid" : "sam:rn:0001"
	});
});

mongoose.connection.on('open', function() {
	console.error('mongo is open');
});

app.listen(3000);
console.log('3000 is the magic port');
