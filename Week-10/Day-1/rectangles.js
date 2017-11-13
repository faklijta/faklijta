'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(a,b) {
    this.a = a;
    this.b = b;
    // this.getArea = function(){
    //     this.area = this.a * this.b
    // }
};

Rectangles.prototype.getArea = function() {
    return this.a * this.b;
};

Rectangles.prototype.getCircumference = function () {
    return 2 * (this.a + this.b)
};

let rectangle = new Rectangles(2, 3);

console.log(rectangle.getArea())
console.log(rectangle.getCircumference())
