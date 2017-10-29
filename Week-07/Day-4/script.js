'use strict'

let galery = [{'title': 'Boys', 'description': 'Cuties', 'url': 'images/img_01.jpg'}, 
{'title': 'Siblings', 'description': 'Under the tree', 'url': 'images/img_02.jpg'},
{'title': 'Alex', 'description': 'Big boy', 'url': 'images/img_03.jpg'},
{'title': 'Us', 'description': 'Our family', 'url': 'images/img_04.jpg'},
{'title': 'Maxim', 'description': 'Thinking', 'url': 'images/img_05.jpg'},
{'title': 'Maxim2', 'description': 'Portrait', 'url': 'images/img_06.jpg'}];

let thumbnails = document.querySelector('.galery');


galery.forEach(function(element, i) {
    let img = document.createElement('img');
    img.style.backgroundImage = 'url(' + galery[i].url + ')';
    img.classList.add('photos');
    thumbnails.appendChild(img);
});
let smallPics = document.querySelectorAll('.photos')
let mainImg = document.querySelector('.main');
let imgIndex = 0;

function bigPic (index) {
    mainImg.style.backgroundImage = 'url(' + galery[imgIndex].url + ')'
}
bigPic();

let toLeft = document.querySelector('.left')
let toRight = document.querySelector('.right')

toLeft.addEventListener('click', function() {
    imgIndex -= 1;
    bigPic();
})

toRight.addEventListener('click', function() {
    imgIndex += 1;
    bigPic();
})

Array.from(smallPics).forEach(function(element, i) {
    element.addEventListener('click', function() {
        imgIndex = i;
        bigPic();
    })
})  

console.log(toLeft)

