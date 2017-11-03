'use strict';
function doRequest(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://cors-anywhere.herokuapp.com/http://secure-reddit.herokuapp.com/posts');
    xhr.onload = function() {
        callback(JSON.parse(xhr.responseText));
    };
    xhr.send();
  }

  function handleData(data){
    console.log(data);
  }

  doRequest(handleData)