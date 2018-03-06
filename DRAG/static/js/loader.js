$(document).ready(function() {
    var twoMinutes = 1000 * 60 * 2;
    $('#big-red-button').click(function() {
        $.blockUI({ message: $('#learning') });
        setTimeout($.unblockUI, twoMinutes);
    });
});