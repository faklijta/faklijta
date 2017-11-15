'use strict';

const playlist = function(){
    let result = [
        { "id": 1, "title": "Favorites", "system": 1}];
    let showCreateDialog = () => {};
    let create = () => {};
    let render = () => {
        result.forEach(function (item) {
            let newPlaylist = document.createElement('h4')
            newPlaylist.textContent = item.title
            document.querySelector('.playlist').appendChild(newPlaylist)
        }
        )};
    let del = () => {};
    let load = () => {};
    let highlight = (i) => {};
    let activePlaylistId;
    let response = [];


    return {
        clickhandler : function(){},
        render: render
    }
    // ajax('GET', 'playlists', render);
};
let newPlaylist = playlist()
newPlaylist.render()


