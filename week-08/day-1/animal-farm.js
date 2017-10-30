class Animal {
    constructor() {
        this.hunger = 5;
        this.thirst = 5;
    }
    eat() {
        this.hunger -= 1;
    }
    drink() {
        this.thirst -= 1;
    }
    play() {
        this.hunger += 1;
        this.thirst += 1;
    }
}
class Farm {
    constructor(slots) {
        this.animals = [];
        this.slots = slots;
    }

    breed () {
        if (this.slots > 0) {
            this.animals.push(new Animal())
        }
        this.slots--;
    }
    slaughter() {
        let fattest = [];
        this.animals.forEach(function(e, i) {
            fattest.push(e.hunger);
        });
        this.animals.splice(fattest.indexOf(Math.min(...fattest)), 1);
        this.slots++;
    }

    print() {
        if (this.animals.length === 0) {
            console.log('We have no animals left, we are bankrupt!');
        } else if (this.animals.length === this.slots) {
            console.log('The farm has', this.animals.length, 'living animals we are full!');
        } else {
            console.log('We have', this.animals.length, 'living animals, we are ok');
        }
    }
    progress() {
        this.animals.forEach(function(e) {
            if (Math.random() > 0.5) {
                e.eat()
            }
            if  (Math.random() > 0.5) {
                e.drink()
            }
            if  (Math.random() > 0.5) {
                e.play()
            }
        });
        this.breed();
        this.slaughter();
        this.print();
    }
}

const SheepFarm = new Farm(20);
for (let i=1; i < 20; i++) {
    SheepFarm.breed();
}
// SheepFarm.progress();
// console.log(SheepFarm.animals);

const button = document.querySelector('button');
button.addEventListener('click', function() {
    SheepFarm.progress();
});
