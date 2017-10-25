'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies
function candyCounter(st_list) {
    let candyHolders = []
    for (let i = 0; i < st_list.length; i++) {
        if (st_list[i]['candies'] > 4) {
            candyHolders.push(st_list[i]['name']);
        }
    } return candyHolders
}
console.log(candyCounter(students));

// create a function that takes a list of students and logs: 
//  - how many candies they have on average
function candyAverage(st_list) {
    let candies = 0;
    for (let i = 0; i < st_list.length; i++) {
        candies += st_list[i]['candies'];
    }
    return candies / st_list.length;
}
console.log(candyAverage(students))