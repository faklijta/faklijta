listOfNumbers = [1, 4];

let summing = function(myArray) {
    total = 0;
    for (i=0; i < myArray.length; i++ ){
        total += myArray[i];
    } return total;
}

module.exports = summing;