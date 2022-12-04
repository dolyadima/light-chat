"use strict";

function get_list_messages() {
    $.ajax({
        type: "GET",
        url: "/list_messages",
        success: function(data) {
            const obj = $.parseJSON(data);
            $("textarea#id_list_messages").val(obj['list_messages']);
        },
        datatype: "json"
    });
}

function send_message() {
    const txt_msg_input = $("input#id_text_message");
    const nickname = $('input#nickname_hidden').val();
    $.ajax({
        type: "POST",
        url: "/new_message",
        data: JSON.stringify({
          'message': nickname + ": " + txt_msg_input.val()
        }),
        contentType: "application/json",
        success: function(){
            txt_msg_input.val("");
        }
    });
}

function set_nickname() {
    const nickname_input = $('input#id_nickname');
    const nickname = nickname_input.val();
    if(nickname !== "") {
        $('input#nickname_hidden').val(nickname);
        nickname_input.val("");
        $('#nickname_div').hide();
        $('#chat_div').show();
    }
}

$(document).ready(function() {
    $('#chat_div').hide();
    setInterval(get_list_messages, 1000);
    setInterval(function() {
        const textarea = $('textarea#id_list_messages');
        textarea.scrollTop(textarea[0].scrollHeight);
        }, 1000);
});
