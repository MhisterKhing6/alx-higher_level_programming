//get the content from a site and display it name
$(function () {
    $.ajax({
        type: "get",
        datatype: 'jsonp',
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        success: function (response) {
            for (i = 0; i < response.results.length; i++) {
                $("UL#list_movies").append('<Li>' + response.results[i].title + '</Li>');
            }
        }
    });
});