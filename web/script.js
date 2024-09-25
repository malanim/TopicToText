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
        $(this).addClass('not_clicable');
        setTimeout(() => {
            $(this).removeClass('not_clicable');
        }, 500);
    });

    $("#del_btn").click(function(){
        eel.delete_temp();
        $(this).removeClass('button-slyled_link');
        $(this).addClass('button-slyled_link_not_clicable');
        setTimeout(() => {
            $(this).removeClass('button-slyled_link_not_clicable');
            $(this).addClass('button-slyled_link');
        }, 2000);
    });
});