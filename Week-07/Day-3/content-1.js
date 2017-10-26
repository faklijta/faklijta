'use strict';
// 1
var heading = document.getElementsByTagName("h1");
console.log(heading)
window.alert(heading[0].innerHTML)
// 2
var allPar = document.querySelectorAll("p");
console.log(allPar[0].textContent)
// 3
var allPar = document.querySelectorAll("p");
window.alert(allPar[1].textContent)
// 4
heading[0].textContent = 'New content';
// 5
[allPar[0].textContent,allPar[2].textContent] = [allPar[2].textContent,allPar[0].textContent];