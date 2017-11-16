'use strict';

const xml = new XMLHttpRequest();
const body = document.querySelector('tbody');
const url = 'http://localhost:3000'

function connectApi(method, resource){
    xml.open(method, url + resource, true);
    xml.onload = function(){
        body.innerHTML = xml.response;
    }
    xml.send();
}

function getData(){
    connectApi('GET', '/all')
}

getData();

