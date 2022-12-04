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
    $.ajax({
        type: "POST",
        url: "/new_message",
        data: JSON.stringify({
          'message': txt_msg_input.val()
        }),
        contentType: "application/json",
        success: function(){
            txt_msg_input.val("");
        }
    });
}

$(document).ready(function() {
    setInterval(get_list_messages, 1000);
});
