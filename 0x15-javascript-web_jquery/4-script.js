//togle the class header if there is a clik on the div tag
$(function () {
    $('DIV#toggle_header').on('click', function () {
        if ($("header").hasClass('red')) {
            $("header").removeClass('red');
            $("header").addClass("green");
        }
        else if ($("header").hasClass('green')) {
            $("header").removeClass('green');
            $("header").addClass("red");
        }
        else {
            $("header").addClass('red');
        }
    });
});