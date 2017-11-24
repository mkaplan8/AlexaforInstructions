$(document).ready(function() {
    // Optimalisation: Store the references outside the event handler:
    var $window = $(window);
    var $pane = $('#pane1');

    function checkWidth() {
        var windowsize = $window.width();
        console.log(windowsize);
        if (windowsize < 1070) {
            $("a.nav-pages").addClass("hover-style");
        } else {
            $("a.nav-pages").removeClass("hover-style");
        }
    }

    // Execute on load
    checkWidth();
    // Bind event listener
    $(window).resize(checkWidth);
});

$("textarea").resizable();
