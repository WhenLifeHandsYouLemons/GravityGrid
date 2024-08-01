const sandColorShift = 0.25;
const sandColorBright = [194, 178, 128];
const sandColorDark = [80, 64, 14];

class Sand {
    constructor(x, y) {
        this.particlePos = [x, y];
        this.particleSpeed = 1;
        this.particleAge = 0;
        this.updated = false;
        this.color = sandColorBright;
    }

    update() {
        if (!this.updated) {
            this.particleAge++;

            this.moveParticle();
            this.changeColor();
            this.updated = true;
        }
    }

    moveParticle() {
        this.particleSpeed = particleSpeed;

        if (this.particleSpeed > 0) {
            // See if it's at the bottom of the screen
            if (this.particlePos[1] + this.particleSpeed >= grid.length) {
                this.particlePos[1] = grid.length - 1;
                grid[this.particlePos[1]][this.particlePos[0]] = this;
                this.particleSpeed = 0;
            }
            // See if it can go down
            else if (grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0]] == 0) {
                grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0]] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[1] += this.particleSpeed;
            }
            // See if it can go down right
            else if (this.particlePos[0] + 1 < grid[0].length && grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] + 1] == 0) {
                grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] + 1] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[1] += this.particleSpeed;
                this.particlePos[0]++;
            }
            // See if it can go down left
            else if (this.particlePos[0] - 1 >= 0 && grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] - 1] == 0) {
                grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] - 1] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[1] += this.particleSpeed;
                this.particlePos[0]--;
            }
            else {
                this.particleSpeed = 0;
            }
        }
    }

    changeColor() {
        if (this.particleSpeed == 0) {
            if (this.color[0] > sandColorDark[0] && this.color[1] > sandColorDark[1] && this.color[2] > sandColorDark[2]) {
                this.color = [this.color[0] - sandColorShift, this.color[1] - sandColorShift, this.color[2] - sandColorShift];
            }
        }
        else {
            if (this.color[0] < sandColorBright[0] && this.color[1] < sandColorBright[1] && this.color[2] < sandColorBright[2]) {
                this.color = [this.color[0] + (sandColorShift * 10), this.color[1] + (sandColorShift * 10), this.color[2] + (sandColorShift * 10)];
            }
        }
    }

    draw() {
        fill(this.color);
        stroke(this.color);
        rect(convertGridToPixels(this.particlePos[0]), convertGridToPixels(this.particlePos[1]), gridSize, gridSize);

        this.updated = false;
    }
}
