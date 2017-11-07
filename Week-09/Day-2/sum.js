listOfNumbers = [1, 4];

let summing = function(myArray) {
    let total = 0;
    if (myArray !== null) {
    for (i=0; i < myArray.length; i++ ){
        total += myArray[i];
    } return total;
} else {
    return new Error("not valid input");
}
};

try {
    summing(null);
}
catch(ex) {
    t.ok(false)
}

module.exports = summing;