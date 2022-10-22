#youtube_python_downloader
# Project for downloading whole Youtube library in MP3 or MP4 format
Follow steps in the tutorial to setup the project
## Tutorial
- Open Youtube playlist video library page in Web browser and open *Developer tools*
- Open *Console* tab and run **part by part** the next code to get playlist *URLS*
### Add JQuery Javascript library to opened page
```js
var jq = document.createElement("script");
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js";
document.getElementsByTagName("head")[0].appendChild(jq);
```
### Fetch and log video urls
```js
$(document).ready(function(){
    var content = "";
    $("#items ytd-playlist-panel-video-renderer").each(function(i, obj){
        content += "https://www.youtube.com" + $(this).children("a").attr("href") + "\n";
    });
    console.log(content);
});
```
- Copy desired video *URLS* and paste them into urls.txt file in the project
- Change the **destination** of files to be saved
- Run the Python script for *MP3* or *MP4* Youtube video download and wait for the process to be completed
