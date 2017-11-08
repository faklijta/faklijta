let express = require('express');
let app = express();
let bodyParser = require('body-parser');
let urlencodedParser = bodyParser.urlencoded({extended :false});

app.use(express.json());
app.use(bodyParser.json());

app.post('/arrays',urlencodedParser, function(request, response) {
    if (request.body.what === 'sum'){
        let sum = 0;
        request.body.numbers.forEach(function(element) {
            sum += element;
        });
        response.json({'result': sum})
    }
    if (request.body.what === 'multiply'){
        let total = 1;
        request.body.numbers.forEach(function(element) {
            total *= element;
        });
        response.json({'result': total})
    }
    if (request.body.what === 'double'){
        let newArray = [];
        request.body.numbers.forEach(function(element) {
            newArray.push(element*2);
        });
        response.json({'result': newArray})
    }
});



app.listen(8080);