/**
 * This js file blocks the machine learning page to allow for
 * a loading screen to be displayed. A JS game inspired by the w3schools
 * example canvas game in HTML5 is used in the loading screen to keep
 * the user entertained.
 *
 * @author James
 * @version 2.0.0
 */

$(document).ready(function () {
    // Calculate two minutes in milliseconds.
    var twoMinutes = 1000 * 60 * 2.5;

    $('#big-red-button').click(function () {
        // When the button is clicked, submit the form.
        $("#machinelearning").find("form").submit();

        // Block the User Interface until ML is finished.
        $.blockUI({message: $('#learning'), css: { top: "10%",
                left: "24%", height: "70%", width: "60%" } });

        // Start the web game.
        startGame();

        // Timeout for UI load.
        setTimeout($.unblockUI, twoMinutes);
    });
});

// The player in the game.
var player;

// The list of obstacles generated.
var barrier = [];

// The current score of the player.
var playerScore;

var gameCanvas = {
    // Make a canvas. Functions are defined
    // to deal with starting of the game, stopping,
    // and clearing the canvas.
    canvas: document.createElement("game-canvas"),
    start: function () {
        this.canvas.width = 500;
        this.canvas.height = 300;

        // Get the canvas context.
        this.context = this.canvas.getContext("2d");
        this.frames = 0;
        var game = document.getElementById("game-area");

        // Append the canvas.
        game.appendChild(this.canvas);
        this.interval = setInterval(updateArea, 20);
    },
    clear: function () {
        this.context.clearRect(0, 0,
            this.canvas.width, this.canvas.height);
    },
    stop: function () {
        clearInterval(this.interval);
    }
};

/**
 * Initiates the game.
 */
function startGame() {
    gameCanvas.start();
    barrier = [];

    // Create a new pixel object to represent the score.
    playerScore = new CreatePlayer("30px", "Consolas",
        "black", 280, 40, "text");

    // Create the actual player object.
    player = new CreatePlayer(30, 30, "red", 10, 120);
}

/**
 * Creates a player object to play the game.
 * @param width    Width of the player in px.
 * @param height   Height of the player in px.
 * @param color    Colour of the player.
 * @param x        Initial x position on canvas.
 * @param y        Initial y position on canvas.
 * @param type     Type of player to create
 * @constructor
 */
function CreatePlayer(width, height, color, x, y, type) {
    this.type = type;
    this.width = width;
    this.height = height;
    this.speedInX = 0;
    this.speedInY = 0;
    this.x = x;
    this.y = y;
    var gameContext = gameCanvas.context;
    gameContext.fillStyle = color;
    gameContext.fillRect(this.x, this.y, this.width, this.height);

    this.update = function () {
        gameContext = gameCanvas.context;

        // If a score type object.
        if(this.type == "text") {
            gameContext.font = this.width + " " + this.height;
            gameContext.fillStyle = color;
            gameContext.fillText(this.text, this.x, this.y);
        }

        // If a player object.
        else {
            gameContext.fillStyle = color;
            gameContext.fillRect(this.x, this.y, this.width, this.height);
        }
    };

    this.newPos = function () {
        // Uses speed of player to update coordinates.
        this.x += this.speedInX;
        this.y += this.speedInY;
    };

    this.collide = function (component) {
        // Handles collision of player and a barrier.
        var currentLeft = this.x;
        var currentRight = this.x + (this.width);
        var currentTop = this.y;
        var currentBottom = this.y + (this.height);
        var otherLeft = component.x;
        var otherRight = component.x + (component.width);
        var otherTop = component.y;
        var otherBottom = component.y + (component.height);
        var crash = true;
        if ((currentBottom < otherTop) ||
            (currentTop > otherBottom) ||
            (currentRight < otherLeft) ||
            (currentLeft > otherRight)) {
            crash = false;
        }
        return crash;
    }
}

/**
 * Updates the playing area.
 */
function updateArea() {
    var x;

    for (var i = 0; i < barrier.length; i++) {
        // Restart the game if the player collides.
        if (player.collide(barrier[i])) {
            gameCanvas.stop();
            gameCanvas.clear();
            startGame();
            return;
        }
    }

    gameCanvas.clear();

    // Increment the frames.
    gameCanvas.frames += 1;

    if (gameCanvas.frames == 1 || checkInterval(100)) {
        x = gameCanvas.canvas.width;

        var minimumHeight = 30;
        var maximumHeight = 170;
        var minimumGap = 30;
        var maximumGap = 170;

        // Generate and add barriers with a height and gap ranging
        // in the above values.
        var height = Math.floor(Math.random() *
            (maximumHeight - minimumHeight + 1) + minimumHeight);
        var gap = Math.floor(Math.random() *
            (maximumGap - minimumGap + 1) + minimumGap);

        // Barries also use the player constructor.
        barrier.push(new CreatePlayer(10, height, "green", x, 0));
        barrier.push(new CreatePlayer(10, (x - height - gap),
            "green", x, (height + gap)));
    }

    for (i = 0; i < barrier.length; i++) {
        barrier[i].x += -1;
        barrier[i].update();
    }

    // Perform respective updates of positions and score.
    playerScore.text = "Score: " + gameCanvas.frames;
    playerScore.update();
    player.newPos();
    player.update();
}

/**
 * Sets upwards velocity.
 */
function moveup() {
    player.speedInY -= 1.5;
}

/**
 * Sets downwards velocity.
 */
function movedown() {
    player.speedInY += 1.5;
}

/**
 * Sets left velocity.
 */
function moveleft() {
    player.speedInX -= 1.5;
}

/**
 * Sets right velocity.
 */
function moveright() {
    player.speedInX += 1.5;
}

/**
 * Stops the players movement.
 */
function stopMove() {
    player.speedInX = 0;
    player.speedInY = 0;
}

/**
 * Checks the frames are correctly aligned.
 *
 * @param currentFrame  The current game frame.
 * @returns {boolean}   True if the frames are divisible by 1.
 */
function checkInterval(currentFrame) {
    return ((gameCanvas.frames / currentFrame) % 1 == 0);
}


