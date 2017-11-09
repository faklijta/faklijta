'use strict';

var express = require('express');
var mysql = require("mysql");
var app = express();
var conn = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "root",
  database: "bookstore"
});

app.use('/assets', express.static('./assets'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/bookstore.html');    
});

app.get('/title', function(req, res) {
    conn.query('SELECT book_name FROM book_mast;', function(error, rows){
        if(error) {
            console.log(error.toString());
        }
        let htmlString = '<tr>';
        rows.forEach(function(row) {
            htmlString = htmlString + '<tr><td>' + row.book_name + '</td></tr>';
        });
        htmlString = htmlString + '</tr>';
        res.send(htmlString)
        });
});


conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.listen(3000);