var ulList = document.querySelector('ul');
var toRemove = document.querySelector('li');
ulList.removeChild(toRemove);
planetData.forEach(function(x) {
    if (x['asteroid']) {
        var newItem = document.createElement('li');
        newItem.classList.add('category');
        newItem.textContent.add('content');
    }
});