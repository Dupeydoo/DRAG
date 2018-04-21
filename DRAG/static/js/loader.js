$(document).ready(function () {
    var twoMinutes = 1000 * 60 * 2.5;

    $('#big-red-button').click(function () {
        $("#machinelearning").find("form").submit();
        $.blockUI({message: $('#learning'), css: { top: "10%", left: "24%", height: "70%", width: "60%" } });
        startGame();
        setTimeout($.unblockUI, twoMinutes);
    });
});


var player;
var barrier = [];
var playerScore;

var gameCanvas = {
    canvas: document.createElement("canvas"),
    start: function () {
        this.canvas.width = 500;
        this.canvas.height = 300;
        this.context = this.canvas.getContext("2d");
        this.frames = 0;
        var game = document.getElementById("game-area");
        game.appendChild(this.canvas);
        this.interval = setInterval(updateArea, 20);
    },
    clear: function () {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    stop: function () {
        clearInterval(this.interval);
    }
};


function startGame() {
    gameCanvas.start();
    barrier = [];
    playerScore = new CreatePlayer("30px", "Consolas", "black", 280, 40, "text");
    player = new CreatePlayer(30, 30, "red", 10, 120);
}


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

        if(this.type == "text") {
            gameContext.font = this.width + " " + this.height;
            gameContext.fillStyle = color;
            gameContext.fillText(this.text, this.x, this.y);
        }

        else {
            gameContext.fillStyle = color;
            gameContext.fillRect(this.x, this.y, this.width, this.height);
        }
    };

    this.newPos = function () {
        this.x += this.speedInX;
        this.y += this.speedInY;
    };

    this.collide = function (component) {
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


function updateArea() {
    var x;

    for (var i = 0; i < barrier.length; i++) {
        if (player.collide(barrier[i])) {
            gameCanvas.stop();
            gameCanvas.clear();
            startGame();
            return;
        }
    }

    gameCanvas.clear();
    gameCanvas.frames += 1;

    if (gameCanvas.frames == 1 || checkInterval(100)) {
        x = gameCanvas.canvas.width;

        var minimumHeight = 30;
        var maximumHeight = 170;
        var minimumGap = 30;
        var maximumGap = 170;

        var height = Math.floor(Math.random() * (maximumHeight - minimumHeight + 1) + minimumHeight);
        var gap = Math.floor(Math.random() * (maximumGap - minimumGap + 1) + minimumGap);

        barrier.push(new CreatePlayer(10, height, "green", x, 0));
        barrier.push(new CreatePlayer(10, (x - height - gap), "green", x, (height + gap)));
    }

    for (i = 0; i < barrier.length; i++) {
        barrier[i].x += -1;
        barrier[i].update();
    }

    playerScore.text = "Score: " + gameCanvas.frames;
    playerScore.update();
    player.newPos();
    player.update();

}


function moveup() {
    player.speedInY -= 1.5;
}


function movedown() {
    player.speedInY += 1.5;
}


function moveleft() {
    player.speedInX -= 1.5;
}


function moveright() {
    player.speedInX += 1.5;
}


function stopMove() {
    player.speedInX = 0;
    player.speedInY = 0;
}


function checkInterval(currentFrame) {
    return ((gameCanvas.frames / currentFrame) % 1 == 0);
}


