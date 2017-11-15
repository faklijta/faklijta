const tracklist = function() {
    let tracks = [
        { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
        { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
    ]
    let render = () => {
        tracks.forEach(function (item) {
            let newTrack = document.createElement('div')
            newTrack.classList = 'track'
            document.querySelector('.tracks').appendChild(newTrack)
            let title = document.createElement('p')
            title.textContent = item.title
            newTrack.appendChild(title)
            let duration = document.createElement('p')
            duration.textContent = item.duration
            newTrack.appendChild(duration)
            // let htmlString =`<!-- <div class="track">
            //     <p>${tracks.title}</p>
            //     <p>${tracks.duration}</p>
            //     </div>`
            // document.querySelector('.tracks').appendChild(htmlString)
        }
        )
    };
        let highlight = () => {};
        let del = () => {};
        // let tracks = [];
        return {
            load: function(){},
            playnext: function(){},
            plaxprev: function(){},
            onPlayClick: function(id){},
            currentTrack : null,
            render: render
        }
};
    let newTracklist = tracklist()
    newTracklist.render()
    