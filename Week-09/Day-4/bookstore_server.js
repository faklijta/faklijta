'use strict';

var express = require('express');
var app = express();

var mysql = require("mysql");

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

app.get('/all', function(req, res) {
    conn.query('SELECT book_name, aut_name, cate_descrip, pub_name,\
                book_price FROM book_mast\
                JOIN author ON author.aut_id=book_mast.aut_id\
                JOIN category ON book_mast.cate_id=category.cate_id \
                JOIN newpublisher ON book_mast.pub_id=newpublisher.pub_id', 
                function(error, rows){
        if(error) {
            console.log(error.toString());
        }
        let htmlString = '<tr>';
        rows.forEach(function(row) {
            htmlString = htmlString + `<tr><td>${row.book_name}</td>
                                      <td>${row.aut_name}</td>
                                      <td>${row.cate_descrip}</td>
                                      <td>${row.pub_name}</td>
                                      <td>${row.book_price}</td>
                                      </tr>`;
        });
        htmlString = htmlString + '</tr>';
        res.send(htmlString)
        });
});

app.get('/q', function(req, res) {
  let searchParam = Object.keys(req.query)[0]
  let searchValue = req.query[searchParam]
  let data = []
  conn.query('SELECT * FROM book_mast where ' +searchParam +"="+ searchValue, function(error, result, fields){
      if(error) {
          console.log(error.toString());
      }
      result.forEach(function(element) {
        data.push(element.book_name)
      });
      res.send(data)
      
})});


conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.listen(3000);