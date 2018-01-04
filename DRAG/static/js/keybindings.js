/**
 * This js file provides the keybind functionality found
 * in the track rating form.
 *
 * @version 2.0.0
 */

$(document).ready(function () {
   var tracks = $(".track").length;          // Get the number of tracks
   addkeybindings(tracks);

    /**
     * Adds keybindings to tracks.
     *
     * @param tracks  Number of tracks.
     */
   function addkeybindings(tracks) {
        for (var i = 0; i < tracks; i++) {
            (function (i) {
                var bind = i + 1;   // Zero indexed so get numeric key to use
                Mousetrap.bind(bind.toString(), function () {          // Bind the numeric key to the function below
                    var track = document.getElementById("track" + i);  // Get the element with the current loop value
                    track.play();
                });
            })(i);
        }

        // AES Grid Keybinds
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

/**
 * Handles a grid key press using the direction input.
 *
 * @param direction  Directional key used.
 * @param tracks     Number of tracks.
 */
function handletrackey(direction, tracks) {
    var gridboundary = tracks - 1;  // The grid is zero indexed so get the boundary
    var element = getgridposition();
    switch (direction) {
        case 0:
            var upnum = setfocus(element) - 4;                // Get where we will focus next
            var upelem = calculatenext(upnum, gridboundary);  // See if its a valid movement
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

/**
 * Gets the current grid position.
 *
 * @returns  The active element in the document, if there is no active element
 *           it returns the first track element.
 */
function getgridposition() {
    // Default focus is focus on the body
    if (document.activeElement.tagName === "BODY") {
        return $("#track0")[0]
    }
    return document.activeElement
}

/**
 * Calculates if the next movement is valid, wraps to zero if not.
 *
 * @param number        The next id to move to.
 * @param gridboundary  The grid boundary.
 * @returns {number}    Where to move next.
 */
function calculatenext(number, gridboundary) {
    // If the number is greater than zero and within the grid boundaries
    return (number > 0 && number <= gridboundary) ? number : 0
}

/**
 * Sets the focus of the next movement by extracting a numeric value from
 * an element id.
 *
 * @param element    The current grid element.
 * @returns {number} The track number of current element.
 */
function setfocus(element) {
    return parseInt(element.id.substring(5)); // The track number is always beyond index 5
}

/**
 * Moves focus to the next element.
 *
 * @param nextelement  The element to move to.
 */
function movefocus(nextelement) {
    var nextelem = $("#track" + nextelement.toString());
    nextelem.focus();   // Apply page focus to the element
}