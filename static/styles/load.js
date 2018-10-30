    window.addEventListener("load", function() {
        document.getElementById("fileupload").onchange = function (event) {
            var oAudio = document.getElementById('audio_core');
            var file = getFilename();
            var extension = file.lastIndexOf('.')
            var title = file.substring(0, extension);
            //alert(title.toString());
            // double check support, and set the
            if (oAudio) {
                oAudio.src = "/static/media/Music/" + file;
                oAudio.load();
                oAudio.play();
                document.getElementById('title').innerHTML = "Title: " + title.toString();
            }
        }
    });





