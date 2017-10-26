'use strict';
// 1
let imageUrl = document.querySelector('img');
console.log(imageUrl.getAttribute('src'))
// 2
imageUrl.setAttribute('src', 'http://www.barathegyisegitokutya.hu/wp-content/uploads/2014/09/kutya_gondozas.jpg')
// 3
let linkRef = document.querySelector('a');
linkRef.setAttribute('href', 'https://www.greenfoxacademy.com/')
// 4
let button = document.querySelectorAll('button');
button[1].disabled = true;
button[1].textContent = "Don't click me!";