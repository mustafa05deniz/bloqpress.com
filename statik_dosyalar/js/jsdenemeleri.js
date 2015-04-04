$(document).ready(function(){
    $("#bir").hide();
    $("#iki").hide();
    $("#button").click(function(){
        $("#bir").toggle("slow");
        $("#iki").toggle("slow");
    });
});