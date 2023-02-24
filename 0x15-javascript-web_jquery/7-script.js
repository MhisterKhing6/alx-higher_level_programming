//get the content from a site and display it name
$(function () {
    $.ajax({
        type: "get",
        datatype: 'jsonp',
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        success: function (response) {
            $("DIV#character").text(response.name);
        }
    });
});