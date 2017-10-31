// Create the multiplier function that you can use like this:
'use strict'
const duplicator = multiplier(2);

function multiplier(x) {
    return function(y) {
        return x * y;
    };
}

console.log(duplicator(5)); // should log 10
console.log(duplicator(10)); // should log 20

// const threeTimes = multiplier(3);
// const double = multiplier(2)
// const sixTimes = (n) => double(threeTimes(n)) 
// const sixTimes = function(n) {
//     return double(threeTimes(n)) 
// }
console.log(sixTimes(2))
console.log(double(threeTimes(3)));

console.log(threeTimes(5)); // should log 15
console.log(threeTimes(100)); // should log 300 