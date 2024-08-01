// Canvas variables
const gridSize = 20;
const backgroundColor = [240, 240, 240];
let canvasWidth, canvasHeight, gridHeight, gridWidth;
let brushSize = 2;

let grid = [];
let particleType = 1;   // 1 for sand, 2 for water, 3 for wall, etc.
const particleSpeed = 1;

function setup() {
    canvasWidth = floor(windowWidth / gridSize) * gridSize;
    canvasHeight = floor(windowHeight / gridSize) * gridSize;

    createCanvas(canvasWidth, canvasHeight);
    background(backgroundColor);

    // Create grid
    gridHeight = floor(windowHeight / gridSize);
    gridWidth = floor(windowWidth / gridSize);

    for (let i = 0; i < gridHeight; i++) {
        grid.push([]);

        for (let j = 0; j < gridWidth; j++) {
            grid[i].push(0);
        }
    }

    spawnRandomParticles(100);

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

    spawnRandomParticles(1);

    if (mouseIsPressed) {
        let gridX = convertPixelsToGrid(mouseX);
        let gridY = convertPixelsToGrid(mouseY);

        if (gridY < grid.length && gridX < grid[0].length && gridY >= 0 && gridX >= 0) {
            if (particleType == 0) {
                removeParticles(gridX, gridY, 2)
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
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] != 0) {
                grid[i][j].draw();
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
    } catch {}
    for (i = 0; i < radius; i++) {
        try {
            grid[y][x+i] = 0;
        } catch {}
        try {
            grid[y][x-i] = 0;
        } catch {}
        try {
            grid[y+i][x] = 0;
        } catch {}
        try {
            grid[y-i][x] = 0;
        } catch {}

        for (j = 0; j < radius; j++) {
            try {
                grid[y+i][x+j] = 0;
            } catch {}
            try {
                grid[y+i][x-j] = 0;
            } catch {}
            try {
                grid[y-i][x-j] = 0;
            } catch {}
            try {
                grid[y-i][x+j] = 0;
            } catch {}
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
