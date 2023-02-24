//get the content from a site and display it name
$(function () {
    $.ajax({
        type: "get",
        datatype: 'jsonp',
        url: "https://fourtonfish.com/hellosalut/?lang=fr",
        success: function (response) {
            $("DIV#hello").text(response.hello);
        }
    });
});