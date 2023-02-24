//Using jquery to change the color of the header
$(function () {
    $("div#toggle_header").on("click", function () {
        $("header").css("color", "#FF0000");
    });
});
