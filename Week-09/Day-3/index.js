let express = require('express');
let app = express();
let bodyParser = require('body-parser');
let urlencodedParser = bodyParser.urlencoded({extended :false});

app.use('/assets', express.static('./assets'));
app.use(bodyParser.json());

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

app.get('/appenda/:input', function(request, response){
    response.json({'appended' : request.params.input + 'a'});
});

app.post('/dountil/:input', urlencodedParser, function(request, response){
    if (request.params.input === 'sum'){
        let sum = 0;
        let num = request.body.until;
        while (num > 0){
            sum += num;
            num--;
        } 
        response.json({'result' : sum});
    }
    if (request.params.input === 'factor'){
        let num = request.body.until;
        let fact = 1;
        while (num > 0){
            fact *= num;
            num--;
        }
        response.json({'result' : fact});
    }
});

app.listen(8080);