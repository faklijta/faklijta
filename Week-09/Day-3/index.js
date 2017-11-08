let express = require('express');
let app = express();

app.use('./assets', express.static('./assets'));

app.get('/', function(request, response) {
    response.sendFile(__dirname + '/index.html');
});


app.listen(3000);