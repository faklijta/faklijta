'use strict'

let galery = [{'title': 'Boys', 'description': 'Cuties', 'url': 'images/img_01.jpg'}, 
{'title': 'Siblings', 'description': 'Under the tree', 'url': 'images/img_02.jpg'},
{'title': 'Alex', 'description': 'Big boy', 'url': 'images/img_03.jpg'},
{'title': 'Us', 'description': 'Our family', 'url': 'images/img_04.jpg'},
{'title': 'Maxim', 'description': 'Thinking', 'url': 'images/img_05.jpg'},
{'title': 'Maxim2', 'description': 'Portrait', 'url': 'images/img_06.jpg'}];

let thumbnails = document.querySelector('.galery');

galery.forEach(function(element) {
    let img = document.createElement('img');
    img.setAttribute('src', element['url']);
    img.classList.add('photos');
    thumbnails.appendChild(img);
});

// let thumbnImage = document.querySelectorAll('photos');
// thumbnImage.forEach(function(element, i) {
//     element.addEventlistener('click', function() {
//         onClick(i);
//     }, false);
// })

let mainImge = document.querySelector('.big-pic');
mainImge.setAttribute('src', 'images/img_01.jpg');