const waterColorShift = 0.25;
const waterColorBright = [100, 100, 255];
const waterColorDark = [50, 50, 145];

class Water {
    constructor(x, y) {
        this.particlePos = [x, y];
        this.particleSpeed = 1;
        this.particleAge = 0;
        this.updated = false;
        this.color = waterColorBright;
        this.direction = 0;     // 0 = none, 1 = left, 2 = right
        this.reachedBottom = false;
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
        // console.log(this.direction);
        this.particleSpeed = particleSpeed;

        if (this.particleSpeed > 0) {
            // See if it's at the bottom of the screen
            if (this.particlePos[1] + this.particleSpeed >= grid.length) {
                this.particlePos[1] = grid.length - 1;
                grid[this.particlePos[1]][this.particlePos[0]] = this;
                this.particleSpeed = 0;
            }

            // See if it can go down
            if (grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0]] == 0) {
                grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0]] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[1] += this.particleSpeed;
            }
            // See if it can go down right
            else if (this.particlePos[0] + 1 < grid[0].length && this.particlePos[1] + this.particleSpeed < grid.length - 1 && grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] + 1] == 0) {
                grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] + 1] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[1] += this.particleSpeed;
                this.particlePos[0]++;
            }
            // See if it can go down left
            else if (this.particlePos[0] - 1 >= 0 && this.particlePos[1] + this.particleSpeed < grid.length - 1 && grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] - 1] == 0) {
                grid[this.particlePos[1] + this.particleSpeed][this.particlePos[0] - 1] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[1] += this.particleSpeed;
                this.particlePos[0]--;
            }
            // See if it can go left
            else if (this.particlePos[0] - 1 >= 0 && grid[this.particlePos[1]][this.particlePos[0] - 1] == 0 && this.direction != 2) {
                grid[this.particlePos[1]][this.particlePos[0] - 1] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[0]--;

                this.direction = 1;
            }
            // See if it can go right
            else if (this.particlePos[0] + 1 < grid[0].length && grid[this.particlePos[1]][this.particlePos[0] + 1] == 0 && this.direction != 1) {
                grid[this.particlePos[1]][this.particlePos[0] + 1] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = 0;

                this.particlePos[0]++;

                this.direction = 2;
            }
            // See if there's a sand particle above it
            else if (grid[this.particlePos[1] - 1][this.particlePos[0]] instanceof Sand) {
                grid[this.particlePos[1] - 1][this.particlePos[0]] = this;
                grid[this.particlePos[1]][this.particlePos[0]] = new Sand(this.particlePos[0], this.particlePos[1]);

                this.particlePos[1]--;
            }
            else {
                this.particleSpeed = 0;
                this.direction = 0;
            }
        }
    }

    changeColor() {
        if (this.particleSpeed == 0) {
            if (this.color[0] > waterColorDark[0] && this.color[1] > waterColorDark[1] && this.color[2] > waterColorDark[2]) {
                this.color = [this.color[0] - waterColorShift, this.color[1] - waterColorShift, this.color[2] - waterColorShift];
            }
        }
        else {
            if (this.color[0] < waterColorBright[0] && this.color[1] < waterColorBright[1] && this.color[2] < waterColorBright[2]) {
                this.color = [this.color[0] + (waterColorShift * 10), this.color[1] + (waterColorShift * 10), this.color[2] + (waterColorShift * 10)];
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
