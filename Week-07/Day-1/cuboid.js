'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

let a = 10;
let b = 10;
let c = 10;

let surface = (a*b + b*c + a*c)*2
let volume = a * b * c;

console.log(surface)
console.log(volume)

