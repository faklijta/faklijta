'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

var fruits = ['apple', 'pear', 'melon', 'grapes'].reverse();
var times = [0, 1, 3, 5];

function toPrint(){
    console.log(fruits.pop())
}
for (let i=0; i<times.length; i++){
    setTimeout(toPrint, i*1000)
}
