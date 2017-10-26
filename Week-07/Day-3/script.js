'use strict';

let button = document.querySelector(".main-button");
let paragraph = document.querySelector(".main-paragraph");

button.addEventListener('click', onClick);

function onClick() {
    paragraph.classList.toggle('changed');
}