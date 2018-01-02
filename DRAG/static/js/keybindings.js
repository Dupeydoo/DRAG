$(document).ready(function () {
   var tracks = $(".track").length;
   addkeybindings(tracks);

   function addkeybindings(tracks) {
        for (var i = 0; i < tracks; i++) {
            (function (i) {
                var bind = i + 1;
                Mousetrap.bind(bind.toString(), function () {
                    var track = document.getElementById("track" + i);
                    track.play();
                });
            })(i);
        }

        Mousetrap.bind({
            'shift+up': function () {
                var direction = 0;
                handletrackey(direction, tracks)
            },
            'shift+down': function () {
                var direction = 1;
                handletrackey(direction, tracks)
            },
            'shift+left': function () {
                var direction = 2;
                handletrackey(direction, tracks)
            },
            'shift+right': function () {
                var direction = 3;
                handletrackey(direction, tracks)
            }
        })
    }
});

function handletrackey(direction, tracks) {
    var gridboundary = tracks - 1;
    var element = getgridposition();
    switch (direction) {
        case 0:
            var upnum = setfocus(element) - 4;
            var upelem = calculatenext(upnum, gridboundary);
            movefocus(upelem);
            break;
        case 1:
            var downnum = setfocus(element) + 4;
            var downelem = calculatenext(downnum, gridboundary);
            movefocus(downelem);
            break;
        case 2:
            var leftnum = setfocus(element) - 1;
            var leftelem = calculatenext(leftnum, gridboundary);
            movefocus(leftelem);
            break;
        case 3:
            var rightnum = setfocus(element) + 1;
            var rightelem = calculatenext(rightnum, gridboundary);
            movefocus(rightelem);
            break;
        default:
            break;
    }
}

function getgridposition() {
    if (document.activeElement.tagName === "BODY") {
        return $("#track0")[0]
    }
    return document.activeElement
}

function calculatenext(number, gridboundary) {
    return (number > 0 && number <= gridboundary) ? number : 0
}

function setfocus(element) {
    return parseInt(element.id.substring(5));
}

function movefocus(nextelement) {
    var nextelem = $("#track" + nextelement.toString());
    nextelem.focus();
}