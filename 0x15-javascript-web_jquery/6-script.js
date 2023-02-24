//Using jquery to change the color of the header
$(function () {
    $("DIV#update_header").on("click", function () {
        $("header").text("New Header!!!");
    });
});
