'use strict';
function doRequest(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:8080/posts');
    xhr.onload = function() {
      let apiResult = JSON.parse(xhr.responseText);
      callback(apiResult);
      console.log(apiResult);
    };
    xhr.send();
  }

  function handleData(data){
    console.log(data);
  }
  function createTempalte(apiData){
    for (let i = 0; i < apiData.posts.length; i++) {
      let title = apiData.posts[i].title;
      let score = apiData.posts[i].score;
      let template = `
      <div class="loaded">
        <div class="vote">
            <div class="upvote"></div>
            <div class="counter">${score}</div>
            <div class="downvote"></div>
        </div>
      <post class="post">
        <h4 class="title">${title}
                <div class="owner">Anonymous</div>
        </h4>
        <div class="buttons">
            <div class="comments">comments</div>
            <div class="modify">modify</div>
            <div class="remove">remove</div>
            <div class="report">report</div>
            <div class="share">share</div>
        </div>
      </post>
      </div>
      `
      let container = document.querySelector('.left');
      let section = document.createElement('section');
      section.innerHTML = template;
      container.appendChild(section);
  }}
  // createTempalte();

  doRequest(createTempalte)