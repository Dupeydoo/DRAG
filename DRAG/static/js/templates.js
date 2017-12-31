$(document).ready(function() {
    var tracks = $(".track").length;
    addkeybindings(tracks);

    $(".smooth").on('click', function(event) {
        if (this.hash !== "") {
          event.preventDefault();

          // Store hash
          var hash = this.hash;
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function(){
            window.location.hash = hash;
          });
        }
      });

    function addkeybindings(tracks) {
        for(var i = 0; i < tracks; i++) {
            (function(i) {
                var bind = i + 1;
                Mousetrap.bind(bind.toString(), function () {
                    var track = document.getElementById("track" + i);
                    track.play();
                });
            })(i);
        }
    }
});