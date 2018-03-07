$(document).ready(function () {
    var twoMinutes = 1000 * 60 * 2;

    $('#big-red-button').click(function () {
        $("#machinelearning").find("form").submit();
        $.blockUI({message: $('#learning')});
        startGame();
        setTimeout($.unblockUI, twoMinutes);
    });
});


var player;
var barrier = [];
var playerScore;


function startGame() {
    playerScore = new CreatePlayer("30px", "Consolas", "black", 280, 40, "text");
    player = new CreatePlayer(30, 30, "red", 10, 120);
    gameCanvas.start();

    Mousetrap.bind("w", moveup(), "keydown");
    Mousetrap.bind("w", stopMove(), "keyup");

    Mousetrap.bind("a", moveleft(), "keydown");
    Mousetrap.bind("a", stopMove(), "keyup");

    Mousetrap.bind("s", movedown(), "keydown");
    Mousetrap.bind("s", stopMove(), "keyup");

    Mousetrap.bind("d", moveright(), "keydown");
    Mousetrap.bind("d", stopMove(), "keyup");
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
            startGame();
            return;
        }
    }

    gameCanvas.clear();
    gameCanvas.frames += 1;

    if (gameCanvas.frames == 1 || checkInterval(100)) {
        x = gameCanvas.canvas.width;

        var minimumHeight = 30;
        var maximumHeight = 200;
        var minimumGap = 40;
        var maximumGap = 200;

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
    player.speedInY -= 1;
}


function movedown() {
    player.speedInY += 1;
}


function moveleft() {
    player.speedInX -= 1;
}


function moveright() {
    player.speedInX += 1;
}


function stopMove() {
    player.speedInX = 0;
    player.speedInY = 0;
}


function checkInterval(currentFrame) {
    return ((gameCanvas.frames / currentFrame) % 1 == 0);
}


var gameCanvas = {
    canvas: document.createElement("canvas"),
    start: function () {
        this.canvas.width = 480;
        this.canvas.height = 270;
        this.context = this.canvas.getContext("2d");
        this.frames = 0;
        var game = document.getElementById("game-area");
        game.insertBefore(this.canvas, document.body.childNodes[0]);
        this.interval = setInterval(updateArea, 20);
    },
    clear: function () {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    stop: function () {
        clearInterval(this.interval);
    }
};


