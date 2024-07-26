// Canvas variables
const gridSize = 20;
const backgroundColor = [240, 240, 240];
let canvasWidth, canvasHeight;

let grid = [];
let particleType = 1;   // 1 for sand, 2 for water, 3 for wall, etc.

function setup() {
    canvasWidth = floor(windowWidth / gridSize) * gridSize;
    canvasHeight = floor(windowHeight / gridSize) * gridSize;

    createCanvas(canvasWidth, canvasHeight);
    background(backgroundColor);

    // Create grid
    let grid_height = floor(windowHeight / gridSize)
    let grid_width = floor(windowWidth / gridSize)

    for (let i = 0; i < grid_height; i++) {
        grid.push([]);

        for (let j = 0; j < grid_width; j++) {
            grid[i].push(0);
        }
    }

    frameRate(60);
}

function draw() {
    background(backgroundColor);

    // Draw mouse cursor
    fill(0, 0, 0);
    stroke(0, 0, 0);
    rect(roundToGrid(mouseX), roundToGrid(mouseY), gridSize, gridSize);

    updateParticles();

    displayParticles();

    spawnParticles(17, 3);

    if (mouseIsPressed) {
        let gridX = convertPixelsToGrid(mouseX);
        let gridY = convertPixelsToGrid(mouseY);

        if (gridY < grid.length && gridX < grid[0].length && gridY >= 0 && gridX >= 0) {
            if (particleType == 0) {
                grid[gridY][gridX] = 0;
                grid[gridY][gridX+1] = 0;
                grid[gridY][gridX-1] = 0;
                grid[gridY+1][gridX] = 0;
                grid[gridY+1][gridX+1] = 0;
                grid[gridY+1][gridX-1] = 0;
                grid[gridY-1][gridX] = 0;
                grid[gridY-1][gridX+1] = 0;
                grid[gridY-1][gridX-1] = 0;
            }
            else if (grid[gridY][gridX] == 0) {
                if (particleType == 1) {
                    grid[gridY][gridX] = new Sand(gridX, gridY);
                }
            }

        }
    }
}

function keyPressed() {
    if (key == '1') {
        particleType = 1;
    }
    else if (key == '0') {
        particleType = 0;
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

function displayParticles() {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] != 0) {
                grid[i][j].show();
            }
        }
    }
}

function spawnParticles(x, y) {
    grid[y][x] = new Sand(x, y);
}

// Conversion functions
function roundToGrid(val) {
    return floor(val / gridSize) * gridSize;
}

function convertGridToPixels(val) {
    return val * gridSize;
}

function convertPixelsToGrid(val) {
    return floor(val / gridSize);
}
