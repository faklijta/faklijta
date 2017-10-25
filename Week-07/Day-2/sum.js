'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(parameter) {
    let result = 0;
    for (let i=1; i <= parameter; i++)
    result += i;
    return result;
}
console.log(sum(3))