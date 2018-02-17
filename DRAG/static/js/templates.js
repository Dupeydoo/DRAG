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
    $(".smooth").on('click', function(event) {
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

    $("#preset select").change(function() {
        
    });
});