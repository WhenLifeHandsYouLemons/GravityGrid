# IMPORTS
import os
import sys
import pygame

# APP WINDOW
colours = {
    "background" : [50, 50, 50],
    "cursor" : [200, 200, 200],
    "sand" : [237, 201, 175],
    "water" : [0, 0, 200]
}

window_height = 620
window_width = 720
window = pygame.display.set_mode((window_width, window_height))

# VARIABLES
particle_size = 10

old_sand_particles = []
sand_speed = 5
max_sand_speed = 30

# CLASSES
class SandParticle:
    x = 0
    y = 0
    time = 0

    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start

    def updateParticle(self):
        self.time += 1
        self.y += self.time * sand_speed

# FUNCTIONS
def create_sand_particle(mouse_pos):
    old_sand_particles.append(SandParticle(mouse_pos[0], mouse_pos[1]))

def draw_sand_particles(sand_particles):
    for particle in sand_particles:
        x = int(particle.split(",")[0])
        y = int(particle.split(",")[1])

        pygame.draw.rect(window, colours["sand"], (x, y, particle_size, particle_size))

def updateParticles():
    

def draw_cursor_pos(mouse_pos):
    x = round(mouse_pos[0] / particle_size) * particle_size
    y = round(mouse_pos[1] / particle_size) * particle_size

    pygame.draw.rect(window, colours["cursor"], (x+particle_size, y, particle_size, particle_size))
    pygame.draw.rect(window, colours["cursor"], (x, y+particle_size, particle_size, particle_size))
    pygame.draw.rect(window, colours["cursor"], (x-particle_size, y, particle_size, particle_size))
    pygame.draw.rect(window, colours["cursor"], (x, y-particle_size, particle_size, particle_size))

# MAIN LOOP
clock = pygame.time.Clock()

running_window = True
while running_window is True:
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_key_state = pygame.mouse.get_pressed()

    window.fill(colours["background"])

    draw_sand_particles(old_sand_particles)
    old_sand_particles = update_sand_particles(old_sand_particles)

    draw_cursor_pos(mouse_pos)

    clock.tick(24)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_window = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_sand_particle(mouse_pos)

pygame.quit()
