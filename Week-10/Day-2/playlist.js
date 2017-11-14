const PlaylistModule = function(dialog) {
    return {
        create: function(playlistName) {
            let newlist = document.createElement('h4')
            newlist.textContent = playlistName
            document.querySelector('.playlist').appendChild(newlist);
            dialog.close();
        }
    }
}