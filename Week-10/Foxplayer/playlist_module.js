const playlist = (function(){
    let result = [
        { "id": 1, "title": "Favorites", "system": 1},
	    { "id": 2, "title": "Music for programming", "system": 0},
	    { "id": 3, "title": "Driving", "system": 0},
	    { "id": 5, "title": "Fox house", "system": 0}];
    let showCreateDialog = () => {};
    let create = () => {};
    let render = () => {
        result.forEach(item) {
            let newPlaylist = document.createElement('h4')
            newPlaylist.textContent = item.title
            document.querySelector('.playlist').appendChild(newPlaylist)
        }
    };
    let del = () => {};
    let load = () => {};
    let highlight = (i) => {};
    let activePlaylistId;
    let response = [];


    return {
        clickhandler : function(){

        }
    }
})();
