# GravityGrid

## About

A 2D grid-based sand and water particle simulator.

## File Directory

`index.html` - The main HTML file that includes the p5.js library and the main script file. Run this file to start the program.

`sketch.js` - The main file where the screen is draw and the game loop exists.

`Sand.js` - The class for the sand particles (includes the update and draw functions)

`Water.js` - The class for the water particles (includes the update and draw functions)

`Wall.js` - The class for the wall particles (includes the draw function)

## Features List

- [x] Sand particles
  - [x] Draw sand particles
  - [x] Create sand particles on click
  - [x] Update sand particles
  - [x] Collision checks
    - [x] With sand
    - [x] With water
    - [x] With walls
  - [x] Duplicate check

- [x] Water particles
  - [x] Draw water particles
  - [x] Create water particles on click
  - [x] Update water particles
  - [x] Collision checks
    - [x] With water
    - [x] With sand
    - [x] With walls
  - [x] Duplicate check

- [x] Wall particles/blocks
  - [x] Draw wall particles
  - [x] Create wall particles on click
  - [x] Duplicate check
