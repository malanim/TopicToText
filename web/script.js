$(function(){

    eel.expose(say);               // Expose this function to Python
    function say(text) {
        $('#status').val(text);
    }

    eel.expose(alert_msg);
    function alert_msg(text) {
        alert(text)
    }
    // say_hello_js("Javascript World!");

//     eel.get_text("connected!");  // Call a Python function
    
    $("#btn").click(function(){

        eel.get_text($("#theme").val(), $("#name").val(), $("#group").val(), $("#colledge").val());
        $('#theme').val('');
        // $('#name').val('');
        // $('#group').val('');
        // $('#colledge').val('');

        // $('#status').val('Successfully!');

    });
}); 