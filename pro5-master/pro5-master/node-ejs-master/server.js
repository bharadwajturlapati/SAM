// load the things we need
var express = require('express');
var app = express();
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

//connect to Mongo DB 
mongoose.connect('localhost', 'pro3');

var A = mongoose.model('A', new Schema({ depth: String, created:Date, site: String,description:String}),'sesmicinfo_quakedetails' );


// set the view engine to ejs
app.set('view engine', 'ejs');

var fs = require('fs');
var path = require('path');
var filePath = path.join(__dirname, 'activity.txt');
var data_mongo = [];

var watch = require('node-watch');
 
watch(filePath, function(req,res) {
	fs.readFile(filePath, function(err,data){
		if (!err){
			
		console.log('received data: ' + data);
		data_mongo = data.toString().split(",");
		console.log(data_mongo);
		var a = new A;
		a.depth=data_mongo[0];
		a.created=data_mongo[1];
		a.site=data_mongo[2];
		a.description=data_mongo[3];
		a.save(function (err, a) {	
		if (err) throw err;
			console.error('saved img to mongo');
		});
		}else{
			console.log(err);
		}
		app.render('pages/live', { dataR:data }, function(err, html){
		});	
	});
	
	
});




app.get('/', function(req, res) {
	fs.readFile(filePath, function(err,data){
		if (!err){
		console.log('received data: ' + data);
		
		}else{
			console.log(err);
		}
		res.render('pages/index',{feed:data});	
	});  
});


mongoose.connection.on('open', function () {
  console.error('mongo is open');
  });




app.listen(8080);
console.log('8080 is the magic port');