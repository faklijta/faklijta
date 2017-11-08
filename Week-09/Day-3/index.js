let express = require('express');
let app = express();

app.use('/assets', express.static('./assets'));

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(request, response){
    if (request.query.input === undefined){
        response.json({'error' : "Please provide an input!"});
    } else{
        response.json({'received' : request.query.input, 'result' : request.query.input*2});
    }
});

app.get('/greeter', function(request, response){
    if (request.query.name === undefined){
        response.json({'error' : "Please provide a name!"});
    }
    if (request.query.title === undefined){
        response.json({'error' : "Please provide a title!"});
    }
    else{
        response.json({'welcome_message' : 'Oh, hi there '+ request.query.name + ', my dear '+ request.query.title +'!'});
    }
});

app.listen(8080);