var fieldSize = 100;
var boardSize = 9;
function setup() {
    console.log(displayWidth);
    console.log(displayHeight);
    createCanvas(displayWidth*pixelDensity(), displayHeight*pixelDensity());

    //stroke(255, 0, 0);
    //strokeWeight(4);
    //rect(0,0, displayWidth, displayHeight);

    setupNewGame();
}


function draw() {

}

function keyPressed() {

}

function setupNewGame()
{
    clear();
    drawMap();
    drawPlayerBoard();
    drawOpponentBoard();
}

var randomColors = ['#6D213C', '#946846', '#BAAB68', '#e3c16f', '#faff70'];
function MapField(x, y, width, height, nr){
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.nr = nr;

    this.draw = function(){
        let c = color(random(randomColors));
        fill(c);
        rect(this.x, this.y, this.width, this.height);
        noFill();
    }
    this.putPlayer = function(colour){
        let c = color(colour);
        fill(c);
        circle(this.x+this.width/2, this.y+this.height/2, 20);
        noFill();
    }
}
var mapFields = [];
var nr = 0;

function drawMap(){
    nr = 0;
    mapFields = [];

    var topRowNumber = floor(displayWidth/fieldSize);
    console.log(topRowNumber);

    // top row
    var spaceLeft = displayWidth-topRowNumber*fieldSize;
    var fieldMargin = spaceLeft/(topRowNumber-1);


    var rect = function(x,y,width,height){
        mapFields.push(new MapField(x,y,width,height,nr));
        nr++;
    }

    rect(0, 0, fieldSize+fieldSize+fieldMargin, fieldSize);
    for(let i=2;i<topRowNumber;i++){
        rect(i*fieldSize + i*fieldMargin, 0, fieldSize, fieldSize);
    }

    var rightColumnNumber = floor(displayHeight/fieldSize);
    var fieldMargin = spaceLeft/(rightColumnNumber-1);
    for(let i=0;i<rightColumnNumber;i++){
        rect(displayWidth-fieldSize, (i+1)*fieldSize, fieldSize, fieldSize);
    }
    var bottomRowNumber = floor(displayWidth/fieldSize);
    var fieldMargin = spaceLeft/(topRowNumber-1);
    for(let i=0;i<bottomRowNumber;i++){
        rect(i*fieldSize + i*fieldMargin, displayHeight-fieldSize, fieldSize, fieldSize);
    }
    var leftColumnNumber = floor(displayHeight/fieldSize)-1;
    var fieldMargin = spaceLeft/(leftColumnNumber-1);
    for(let i=0;i<leftColumnNumber-1;i++){
        rect(0, displayHeight-(i+1)*fieldSize, fieldSize, fieldSize);
    }
    rect(0, fieldSize, fieldSize, fieldSize+(displayHeight-((leftColumnNumber+1)*fieldSize)));
    console.log(mapFields);
    for(let i=0;i<mapFields.length;i++){
        mapFields[i].draw();
    }
    mapFields[10].putPlayer('red');
}

function BoardField(x, y, width, height, coord_x, coord_y){
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;
    this.coord_x = coord_x;
    this.coord_y = coord_y;

    this.draw = function(){
        rect(this.x, this.y, this.width, this.height);
    }
    this.putPiece = function(colour){
        let c = color(colour);
        fill(c);
        circle(this.x+this.width/2, this.y+this.height/2, 20);
        noFill();
    }
}

var playerBoardFields = [];
function drawPlayerBoard(player){
    var y = fieldSize*3.5;
    var x = fieldSize*1.5;
    var boardFieldSize = fieldSize*0.65;

    button = createButton('Skip');
    button.position(x, y-fieldSize);
    //button.mousePressed(skip);
    button.class('btn-info btn');

    button = createButton('flip');
    button.position(x+fieldSize, y-fieldSize);
    //button.mousePressed(setupNewGame);
    button.class('btn-info btn');

    button = createButton('rotate');
    button.position(x+2*fieldSize, y-fieldSize);
    //button.mousePressed(setupNewGame);
    button.class('btn-info btn');

    textSize(64);
    fill('black');
    t = text('00:00', x, y-1.7*fieldSize);
    noFill();
    

    for(let i=0;i<boardSize;i++){
        for(let j=0;j<boardSize;j++){
            let bf = new BoardField(x+j*boardFieldSize, y+i*boardFieldSize, boardFieldSize, boardFieldSize, j, i);
            playerBoardFields.push(bf);
        }
    }
    for(let i=0;i<playerBoardFields.length;i++){
        playerBoardFields[i].draw();

    }
}

var opponentBoardFields = [];
function drawOpponentBoard(player){
    var y = fieldSize*5;
    var boardFieldSize = fieldSize*0.5;
    var x = displayWidth-fieldSize*1.5-boardFieldSize*boardSize;

    textSize(32);
    fill('black');
    t = text('00:00', x+boardFieldSize*7, y - fieldSize*0.3);
    noFill();

    for(let i=0;i<boardSize;i++){
        for(let j=0;j<boardSize;j++){
            let bf = new BoardField(x+j*boardFieldSize, y+i*boardFieldSize, boardFieldSize, boardFieldSize, j, i);
            opponentBoardFields.push(bf);
        }
    }
    for(let i=0;i<opponentBoardFields.length;i++){
        opponentBoardFields[i].draw();
    }
}
