/*
When a file is selected, the first function will run.
This essentially grabs the text value of the selected file and:
    1. Trims unnecessary white space from the front (not sure why it was there, but it was)
    2. Sends that trimmed string to the chained function load(string)
 */
$(document).ready(function(){
    $('#songpicker').on('change', function() {
        var optionText = $("#songpicker option:selected").text();
        var strOptionText = optionText.toString().trim();

        load(strOptionText);
    })
});

/*
From here, we grab the information for the audio player on the web page and:
    1. We update the audio source with the new path '/static/media/music/(the trimmed title string)
    2. Load the audio player with this new file
    3. Automatically begin playing the selected track
    4. Edit the inner html of the title tag for the music player to reflect the currently playing song
*/
function load(title) {
    var oAudio = document.getElementById('audio_core');
    var extension = title.lastIndexOf('.');
    var cleanTitle = title.substring(0, extension);
    if (oAudio) {
        oAudio.src = "/static/media/Music/" + title;
        oAudio.load();
        oAudio.play();
        document.getElementById('title').innerHTML = "Title: " + cleanTitle.toString();
    }};
/*
Reflection: This could probably be done in one function but I don't really care anymore.
LINKS:
Trimming:
https://css-tricks.com/snippets/javascript/strip-whitespace-from-string/
Grab text from select tag:
https://www.codexworld.com/how-to/get-text-value-of-selected-option-using-jquery/
DO NOT DELETE THIS
    window.addEventListener("load", function() {
        document.getElementById("songpicker").onchange = function (event) {
            var oAudio = document.getElementById('audio_core');
            var file = getFilename();
            var extension = file.lastIndexOf('.')
            var title = file.substring(0, extension);
            alert(title.toString());
            // double check support, and set the
            if (oAudio) {
                oAudio.src = "/static/media/Music/" + file;
                oAudio.load();
                oAudio.play();
                document.getElementById('title').innerHTML = "Title: " + title.toString();
            }
        }
    });
*/