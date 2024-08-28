const wallColor = [127, 127, 127];

class Wall {
    constructor(x, y) {
        this.type = 'wall';
        this.particlePos = [x, y];
    }

    update() {
        // Do nothing
    }

    draw() {
        fill(wallColor);
        stroke(wallColor);
        rect(convertGridToPixels(this.particlePos[0]), convertGridToPixels(this.particlePos[1]), gridSize, gridSize);
    }
}