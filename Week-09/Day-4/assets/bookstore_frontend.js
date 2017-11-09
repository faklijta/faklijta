'use strict';
const xml = new XMLHttpRequest();
const body = document.querySelector('tbody');
const url = 'http://localhost:3000'

function talkToAPI(method, resource){
    xml.open(method, url + resource, true);
    xml.onload = function(){
        body.innerHTML = xml.response;
    }
    xml.send();
}


function getList(){
    talkToAPI('GET', '/title')
}

getList();