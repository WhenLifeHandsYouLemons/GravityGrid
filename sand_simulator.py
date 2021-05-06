"""
Made by - Sooraj.S
GitHub - https://github.com/WhenLifeHandsYouLemons
Twitter - https://twitter.com/LemonsHandYou
Instagram - https://www.instagram.com/whenlifehandsyoulemons1/
Latest Release - https://github.com/WhenLifeHandsYouLemons/Particle-Simulator/releases
"""

"""
IMPORTS
"""
import os
import sys
import pygame

"""
FILE SEARCHING USED IN '.exe' FORMAT
"""
def get_true_filename(filename):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath('.')
    return os.path.join(base, filename)

"""
APP WINDOW
"""
bg_colour = 50, 50, 50
window_height = 620
window_width = 620
WIN = pygame.display.set_mode((window_width, window_height))
WIN.fill(bg_colour)

"""
VARIABLES
"""
border_colour = 0, 0, 0

def border():
    pygame.draw.rect(WIN, border_colour, (0, 0, 10, 620))
    pygame.draw.rect(WIN, border_colour, (0, 0, 620, 10))
    pygame.draw.rect(WIN, border_colour, (610, 0, 10, 620))
    pygame.draw.rect(WIN, border_colour, (0, 610, 620, 10))

particle_size_x = 10
particle_size_y = particle_size_x

sand_colour = (237, 201, 175)

def draw_sand_particles():
    if mouse_key_state[0]:
        pygame.draw.rect(WIN, sand_colour, (new_particle_pos_x, new_particle_pos_y, particle_size_x, particle_size_y))
        info_append = f"({new_particle_pos_x}, {new_particle_pos_y})0"
        old_sand_particles.append(info_append)

def get_keys_mouse():
    global key
    global mouse_pos
    global mouse_key_state
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_key_state = pygame.mouse.get_pressed()
    global new_particle_pos_x
    global new_particle_pos_y
    new_particle_pos_x = mouse_pos[0]
    new_particle_pos_x = round(mouse_pos[0] / 10) * 10
    new_particle_pos_y = round(mouse_pos[1] / 10) * 10

old_sand_particles = []
new_sand_particles = []
max_sand_speed = 30

def sand_physics():
    print(f"Number of particles: {len(old_sand_particles)}")
    pygame.Surface.fill(WIN, bg_colour)
    for particle in old_sand_particles:
        particle_info = particle.split(")")
        particle_time = int(particle_info[1])
        new_particle_time = particle_time + 1
        sand_speed = round(int((0.5 * new_particle_time) ** 2) / 10) * 10
        if sand_speed > max_sand_speed:
            sand_speed = max_sand_speed
        particle_pos = particle_info[0].split("(")
        particle_pos = particle_pos[1].split(", ")
        particle_pos_x = float(particle_pos[0])
        particle_pos_y = int(particle_pos[1])
        particle_pos_y = particle_pos_y + sand_speed

        if particle_pos_x > 0 and particle_pos_x < window_width and particle_pos_y > 0 and particle_pos_y < window_width:
            pygame.draw.rect(WIN, sand_colour, (particle_pos_x, particle_pos_y, particle_size_x, particle_size_y))
            new_info_append = f"({particle_pos_x}, {particle_pos_y}){new_particle_time}"
            new_sand_particles.append(new_info_append)
    reset_sand_particles()

def reset_sand_particles():
    old_sand_particles.clear()
    index = 0
    while index != len(new_sand_particles):
        old_sand_particles.append(new_sand_particles[index])
        new_sand_particles.pop(0)

"""
SETS FPS
"""
clock = pygame.time.Clock()

"""
MAIN LOOP
"""
RUNNING_WINDOW = True

while RUNNING_WINDOW == True:
    clock.tick(30)

    get_keys_mouse()
    sand_physics()
    border()
    draw_sand_particles()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
            pygame.quit()



sys.exit()
