var jquery = document.createElement("script");
jquery.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js";
document.getElementsByTagName("head")[0].appendChild(jquery);


$(document).ready(function(){
    var content = "";
    $("#items ytd-playlist-panel-video-renderer").each(function(i, obj){
        content += "https://www.youtube.com" + $(this).children("a").attr("href") + "\n";
    });
    console.log(content);
});



$(document).ready(function(){
    $("#items ytd-playlist-panel-video-renderer").each(function(i, obj){
        var element = "<iframe class='dwns' src='" + "https://www.youtube.com" + $(this).children("a").attr("href") + "' width='100%' height='100%' allowtransparency='true' scrolling='no' style='border:none'></iframe>";
        $("#primary").append(element);
    });
});
