let mysql = require("mysql");
let express = require("express");
let app = express();

let conn = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Alex1124",
  database: 'bookstore'
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
  }
  else {
    console.log("Connection established");
  }
});

// conn.query("SELECT book_name FROM book_mast;",function(err,rows){
//     console.log("Data received from Db:\n");
//     console.log(rows);
// });

app.get('/', function(req, res) {
  conn.query('SELECT book_name FROM book_mast;',function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(rows);
  });
});

app.listen(3000);
