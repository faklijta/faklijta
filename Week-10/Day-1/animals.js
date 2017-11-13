'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function talk(){

    console.log(this.sound)
}

let animal = {
    talk
}

let cat = {
    sound: 'meow!'
}

let dog = {
    sound: 'woof!'
}

Object.setPrototypeOf(cat, animal)
Object.setPrototypeOf(dog, animal)

cat.talk()
dog.talk()