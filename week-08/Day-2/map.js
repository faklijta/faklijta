'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

let eCounter = fruits.map(function(x){
    let eNums = x.split('').filter(function(y){
        if (y === 'e') {
            return y;
        }
    })
    return eNums.length
});
console.log(eCounter)
// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method
