class Sharpie {

    constructor(color, width) {
        this.color = color;
        this.width = width;
        this.inkAmount = 100;
    }

    use() {
        this.inkAmount -= this.width;
    }
}

var greenSharpie = new Sharpie('green', 10);

while (greenSharpie.inkAmount >= greenSharpie.width) {
    greenSharpie.use();
    console.log(greenSharpie.inkAmount);
}