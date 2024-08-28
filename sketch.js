// Canvas variables
const gridSize = 25;
const backgroundColor = [240, 240, 240];
let canvasWidth, canvasHeight, gridHeight, gridWidth;
let brushSize = 1;

let grid = [];
let particleTypes = {
    1: "Sand",
    2: "Water",
    3: "Wall",
    0: "Eraser"
};
let particleType = 1;   // 1 for sand, 2 for water, 3 for wall, 0 for destroying particles
const particleSpeed = 1;
let particleCount = 0;
let raining = false;

function setup() {
    canvasWidth = floor(windowWidth / gridSize) * gridSize;
    canvasHeight = (floor(windowHeight / gridSize) * gridSize);

    createCanvas(canvasWidth, canvasHeight);
    background(backgroundColor);

    // Create grid
    gridHeight = floor(windowHeight / gridSize);
    gridWidth = floor(windowWidth / gridSize);

    resetGrid();

    createOptions();

    frameRate(60);
}

function draw() {
    background(backgroundColor);

    // Draw mouse cursor
    fill(0, 0, 0);
    stroke(0, 0, 0);
    rect(roundToGridPixels(mouseX), roundToGridPixels(mouseY), gridSize, gridSize);

    updateParticles();

    drawParticles();

    addRain();

    if (mouseIsPressed) {
        let gridX = convertPixelsToGrid(mouseX);
        let gridY = convertPixelsToGrid(mouseY);

        if (gridY < grid.length && gridX < grid[0].length && gridY >= 0 && gridX >= 0) {
            if (particleType == 0) {
                removeParticles(gridX, gridY, brushSize)
            }
            else if (grid[gridY][gridX] == 0) {
                if (particleType == 1) {
                    grid[gridY][gridX] = new Sand(gridX, gridY);
                }
                else if (particleType == 2) {
                    grid[gridY][gridX] = new Water(gridX, gridY);
                }
                else if (particleType == 3) {
                    grid[gridY][gridX] = new Wall(gridX, gridY);
                }
            }

        }
    }

    // Draw UI
    drawUI();
}

function drawUI() {
    fill(0, 0, 0);
    stroke(0, 0, 0);
    textFont('Arial');
    textSize(20);

    textAlign(LEFT);
    text("GravityGrid", 10, 30);

    textAlign(RIGHT);
    text("Particle type: " + particleTypes[particleType], canvasWidth - 10, 30);
    text("Total particle count: " + particleCount, canvasWidth - 10, 60);
    text("Eraser size: " + brushSize, canvasWidth - 10, 90);
}

function keyPressed() {
    if (key == '0') {
        particleType = 0;
    }
    else if (key == '1') {
        particleType = 1;
    }
    else if (key == '2') {
        particleType = 2;
    }
    else if (key == '3') {
        particleType = 3;
    }
    else if (key == ' ') {
        if (isLooping()) {
            noLoop();
        }
        else {
            loop();
        }
    }
    else if (key == 'ArrowRight') {
        noLoop();
        draw();
    }
    else if (key == 'c') {
        resetGrid();
    }
    else if (key == '=') {
        brushSize++;
        if (brushSize > 10) {
            brushSize = 10;
        }
    }
    else if (key == '-') {
        brushSize--;
        if (brushSize < 1) {
            brushSize = 1;
        }
    }
    else if (key == 'r') {
        raining = !raining;
    }
}

function updateParticles() {
    for (let j = 0; j < grid[0].length; j++) {
        for (let i = grid.length - 1; i >= 0; i--) {
            if (grid[i][j] != 0) {
                grid[i][j].update();
            }
        }
    }
}

function drawParticles() {
    particleCount = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] != 0) {
                grid[i][j].draw();
                particleCount++;
            }
        }
    }
}

function spawnParticles(x, y) {
    if (grid[y][x] == 0) {
        if (particleType == 1) {
            grid[y][x] = new Sand(x, y);
        }
        if (particleType == 2) {
            grid[y][x] = new Water(x, y);
        }
    }
}

function spawnRandomParticles(quantity) {
    for (i = 0; i < quantity; i++) {
        spawnParticles(round(random(0, gridWidth - 1)), round(random(0, gridHeight / 4)));
    }
}

function removeParticles(x, y, radius) {
    try {
        grid[y][x] = 0;
    } catch { }

    for (i = 0; i < radius; i++) {
        try {
            grid[y][x + i] = 0;
        } catch { }
        try {
            grid[y][x - i] = 0;
        } catch { }
        try {
            grid[y + i][x] = 0;
        } catch { }
        try {
            grid[y - i][x] = 0;
        } catch { }

        for (j = 0; j < radius; j++) {
            try {
                grid[y + i][x + j] = 0;
            } catch { }
            try {
                grid[y + i][x - j] = 0;
            } catch { }
            try {
                grid[y - i][x - j] = 0;
            } catch { }
            try {
                grid[y - i][x + j] = 0;
            } catch { }
        }
    }
}

function addRain() {
    if (raining) {
        spawnRandomParticles(1);
    }
}

function resetGrid() {
    grid = [];

    for (let i = 0; i < gridHeight; i++) {
        grid.push([]);

        for (let j = 0; j < gridWidth; j++) {
            grid[i].push(0);
        }
    }
}

function createOptions() {
    createP();
    createButton('Sand').mousePressed(() => particleType = 1);
    createButton('Water').mousePressed(() => particleType = 2);
    createButton('Wall').mousePressed(() => particleType = 3);

    createP();
    createButton('Eraser').mousePressed(() => particleType = 0);
    createButton('Increase erase size').mousePressed(() => brushSize++);
    createButton('Decrease erase size').mousePressed(() => brushSize--);

    createP();
    createButton('Start/Stop').mousePressed(() => isLooping() ? noLoop() : loop());
    createButton('Clear').mousePressed(() => resetGrid());
    createButton('Toggle Rain').mousePressed(() => raining = !raining);

    createP();
    createButton('Save grid state').mouseClicked(() => saveStateFile());
    createP('Load grid state:');
    createFileInput(loadStateFile);

    createP('Press <kbd>1</kbd>, <kbd>2</kbd>, <kbd>3</kbd>, <kbd>0</kbd> to change particle type. Press <kbd>Space</kbd> to start/stop simulation. Press <kbd>Right Arrow</kbd> to step forward through the simulation.');

    createP('Made and hosted by <a href="https://sooraj.dev/">Sooraj</a>.');
}

function saveStateFile() {
    saveJSON(grid, 'GravityGrid Grid State.json');
}

function loadStateFile(file) {
    resetGrid();

    // Parse the file and load the grid
    if (file.type === 'application') {
        let data = file.data;

        for (let i = 0; i < min(grid.length, data.length); i++) {
            for (let j = 0; j < min(grid[i].length, data[i].length); j++) {
                if (data[i][j] != 0) {
                    let particle = data[i][j];

                    if (particle.type == 'sand') {
                        grid[i][j] = new Sand(j, i, particle['particleSpeed'], particle['particleAge'], particle['updated'], particle['color']);
                    }
                    else if (particle.type == 'water') {
                        grid[i][j] = new Water(j, i, particle['particleSpeed'], particle['particleAge'], particle['updated'], particle['color'], particle['direction'], particle['reachedBottom']);
                    }
                    else if (particle.type == 'wall') {
                        grid[i][j] = new Wall(j, i);
                    }
                }
            }
        }
    }
}

// Conversion functions
function roundToGridPixels(val) {
    return floor(val / gridSize) * gridSize;
}

function convertGridToPixels(val) {
    return val * gridSize;
}

function convertPixelsToGrid(val) {
    return floor(val / gridSize);
}
