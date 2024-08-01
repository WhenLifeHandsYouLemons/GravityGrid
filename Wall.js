const wallColor = [127, 127, 127];

class Wall {
    constructor(x, y) {
        this.particlePos = [x, y];
        this.color = wallColor;
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