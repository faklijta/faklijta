let express = require('express');
let app = express();

app.use('/assets', express.static('./assets'));

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(request, response){
    response.json({'received' : request.query.input, 'result' : request.query.input*2});
});


app.listen(8080);