/**
 * This js file provides general functionality to html files.
 *
 * @version 1.0.0
 */

$(document).ready(function () {
    /**
     * This function binds a smooth scroll to the
     * click on class .smooth links.
     *
     * @param event      The event bound to.
     * @param eventfunc  The function that runs.
     */
    $(".smooth").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();  // Prevent the default behaviour for clicking this class

            // Store id hash
            var hash = this.hash;
            // Perform the scroll
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function () {
                window.location.hash = hash;
            });
        }
    });

    $(document).scroll(function () {
        if ($(window).scrollTop() === 0) {
            $('#scroller').fadeOut();
        }

        else {
            $('#scroller').fadeIn();
        }
    });


    $(window).scroll(function () {
        checkAnimation();
    });

    $("a[href='#']").click(function () {
        $('html, body').animate({scrollTop: 0}, 'slow');
        return false;
    });

    $(".form-control").change(function () {
        $(this).addClass("confirmed");
    });
});

function isElementInViewport(elem) {
    var $elem = $(elem);
    var scrollElem = ((navigator.userAgent.toLowerCase().indexOf('webkit') != -1) ? 'body' : 'html');
    var viewportTop = $(scrollElem).scrollTop();
    var viewportBottom = viewportTop + $(window).height();
    var elemTop = Math.round($elem.offset().top);
    var elemBottom = elemTop + $elem.height();
    return ((elemTop < viewportBottom) && (elemBottom > viewportTop));
}

function checkAnimation() {
    var $elem = $('.about-section img');
    if ($elem.hasClass('rollIn animated')) return;
    if (isElementInViewport($elem)) {
        $elem.addClass('rollIn animated');
    }
}