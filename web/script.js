$(function(){

    eel.expose(say);
    function say(text) {
        $('#status').val(text);
    }

    eel.expose(alert_msg);
    function alert_msg(text) {
        alert(text)
    }

//     eel.get_text("connected!");
    
    $("#btn").click(function(){
        eel.get_text($("#theme").val(), $("#name").val(), $("#group").val(), $("#colledge").val());
        $('#theme').val('');
        // $('#name').val('');
        // $('#group').val('');
        // $('#colledge').val('');
    });
}); 