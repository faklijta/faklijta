'use strict';

var express = require('express');
var app = express();
app.use('/', express.static('./'));
express.json.type = "application/json";
app.use(express.json());
const mysql = require("mysql");

const conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "root",
    database: "Foxplayer"
  });

conn.connect(function(err){
if(err){
    console.log("Error connecting to Db");
    return;
}
console.log("Connection to audio database established");
});


app.get('/', function(req, res) {
    res.sendFile(__dirname + 'index.html');    
});

app.get('/playlists', function(req, res) {
    let result = [];
        const query = "SELECT * FROM playlists";
        conn.query(query, function(err,rows){
          if(err) {
            console.log("PARA", err.toString());
            return;
          } else {
            rows.forEach(row => {
              result.push(row);
            });
          }
          res.send(result);
        });
});

app.get('/tracklist', function get(req, res){

    let result = [];
    const query = "SELECT * FROM tracklist";
    conn.query(query, function(err,rows){
      if(err) {
        console.log("Error", err.toString());
        return;
      } else {
        rows.forEach(row => {
          result.push(row);
        });
      }
      res.send(result);
    });
  });

app.listen(3000, function(){
    console.log( 'Server is running');
});