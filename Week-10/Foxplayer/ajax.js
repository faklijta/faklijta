'use strict';

const url = 'http://localhost:3000/';

const ajaxGet = function (command, urlEnd, callback) {
    let command = 'GET';
    let xhr = new XMLHttpRequest();
    xhr.open(command, url + urlEnd);
    xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');
    xhr.onload = function() {
        callback(JSON.parse(xhr.responseText));
    };
    xhr.send();
};

const ajaxPost = function (command, urlEnd, callback) {
    let command = 'POST';
    let xhr = new XMLHttpRequest();
    xhr.open(command, url + urlEnd);
    xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.setRequestHeader('Accept', 'application/json');
    xhr.onload = function() {
        callback(JSON.parse(xhr.responseText));
    };
    xhr.send();
};


