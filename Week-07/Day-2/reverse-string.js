'use strict';
// Reverse the string!

var reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
function reverseString(str) {
    var splitString = reversed.split(""); 
    var reverseArray = splitString.reverse();
    var joinArray = reverseArray.join("");
    return joinArray;
}
console.log(reverseString(reversed))