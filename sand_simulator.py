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
window_width = 720
WIN = pygame.display.set_mode((window_width, window_height))
WIN.fill(bg_colour)

"""
VARIABLES
"""
border_colour = 0, 0, 0
border_thickness = 10
border_particles = ["(0, 610)", "(10, 610)", "(20, 610)", "(30, 610)", "(40, 610)", "(50, 610)", "(60, 610)", "(70, 610)", "(80, 610)", "(90, 610)", "(100, 610)", "(110, 610)", "(120, 610)", "(130, 610)", "(140, 610)", "(150, 610)", "(160, 610)", "(170, 610)", "(180, 610)", "(190, 610)", "(200, 610)"]

def border():
    # Left border
    pygame.draw.rect(WIN, border_colour, (0, 0, border_thickness, window_height))
    # Top border
    pygame.draw.rect(WIN, border_colour, (0, 0, window_width - 110, border_thickness))
    # Right border
    pygame.draw.rect(WIN, border_colour, (window_width - 110, 0, border_thickness, window_height))
    # Bottom border
    pygame.draw.rect(WIN, border_colour, (0, window_height - 10, window_width - 110, border_thickness))

particle_size_x = 10
particle_size_y = particle_size_x

sand_colour = (237, 201, 175)

def draw_sand_particles():
    if mouse_key_state[0]:
        # pygame.time.wait(80)
        info_append = f"({new_particle_pos_x}, {new_particle_pos_y})0"
        pygame.draw.rect(WIN, sand_colour, (new_particle_pos_x, new_particle_pos_y, particle_size_x, particle_size_y))
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

def mouse_cursor():
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(WIN, (255, 255, 255), (round(mouse_pos[0] / 10) * 10 - 10, round(mouse_pos[1] / 10) * 10, particle_size_x, particle_size_y))
    pygame.draw.rect(WIN, (255, 255, 255), (round(mouse_pos[0] / 10) * 10 + 10, round(mouse_pos[1] / 10) * 10, particle_size_x, particle_size_y))
    pygame.draw.rect(WIN, (255, 255, 255), (round(mouse_pos[0] / 10) * 10, round(mouse_pos[1] / 10) * 10 - 10, particle_size_x, particle_size_y))
    pygame.draw.rect(WIN, (255, 255, 255), (round(mouse_pos[0] / 10) * 10, round(mouse_pos[1] / 10) * 10 + 10, particle_size_x, particle_size_y))

old_sand_particles = []
new_sand_particles = []
max_sand_speed = 30
sand_speed = 5

def sand_physics():
    print(f"Number of particles: {len(old_sand_particles)}")
    pygame.Surface.fill(WIN, bg_colour)
    row = window_height - border_thickness - 10
    while row != 0:
        column = border_thickness
        while column != 610:
            particle = 0
            while particle != len(old_sand_particles):
                current_particle_info = old_sand_particles[particle]
                current_particle_info = current_particle_info.split(")")
                old_current_particle_time = int(current_particle_info[1])
                new_current_particle_time = old_current_particle_time + 1
                sand_speed = round(int((0.5 * new_current_particle_time) ** 2) / 10) * 10
                if sand_speed > max_sand_speed:
                    sand_speed = max_sand_speed
                current_particle_info = current_particle_info[0]
                current_particle_info = current_particle_info.split("(")
                current_particle_info = current_particle_info[1]
                current_particle_info = current_particle_info.split(", ")
                current_particle_pos_x = int(current_particle_info[0])
                old_current_particle_pos_y = int(current_particle_info[1])
                new_current_particle_pos_y = old_current_particle_pos_y + sand_speed
                if current_particle_pos_x == column and new_current_particle_pos_y == row:
                    # print("Found matching particle position!")
                    particle_check = 0
                    while particle_check != len(old_sand_particles) - 1:
                        if particle_check == particle:
                            particle_check = particle_check + 1
                        elif particle_check + 1 >= len(old_sand_particles):
                            particle_check = len(old_sand_particles) - 1
                            return
                        under_particle_info = old_sand_particles[particle_check]
                        under_particle_info = under_particle_info.split(")")
                        under_particle_info = under_particle_info[0]
                        under_particle_info = under_particle_info.split("(")
                        under_particle_info = under_particle_info[1]
                        under_particle_info = under_particle_info.split(", ")
                        under_particle_pos_x = int(under_particle_info[0])
                        under_particle_pos_y = int(under_particle_info[1])
                        if under_particle_pos_y == new_current_particle_pos_y:
                            new_current_particle_pos_y = under_particle_pos_y - 10
                            new_current_particle_time = 0
                            particle_check = 0
                            if particle_check == particle:
                                particle_check = particle_check + 1
                        else:
                            particle_check = particle_check + 1
                    pygame.draw.rect(WIN, sand_colour, (current_particle_pos_x, new_current_particle_pos_y, particle_size_x, particle_size_y))
                    new_info_append = f"({current_particle_pos_x}, {new_current_particle_pos_y}){new_current_particle_time}"
                    new_sand_particles.append(new_info_append)
                    particle = len(old_sand_particles)
                else:
                    particle = particle + 1
            column = column + 10
        row = row - 10
    reset_sand_particles()

def reset_sand_particles():
    old_sand_particles.clear()
    index = 0
    while index != len(new_sand_particles):
        count = 1
        while count != len(new_sand_particles):
            index_particle_pos = new_sand_particles[index].split(")")
            index_particle_pos = index_particle_pos[0]
            count_particle_pos = new_sand_particles[count].split(")")
            count_particle_pos = count_particle_pos[0]
            if index_particle_pos == count_particle_pos:
                new_sand_particles.pop(count)
                count = 1
            else:
                count = count + 1
        old_sand_particles.append(new_sand_particles[index])
        new_sand_particles.pop(0)

"""
DEBUGGING BLOCKS
"""
info_append = "(200, 50)0"
pygame.draw.rect(WIN, sand_colour, (200, 50, particle_size_x, particle_size_y))
old_sand_particles.append(info_append)

info_append = "(200, 100)0"
pygame.draw.rect(WIN, sand_colour, (200, 100, particle_size_x, particle_size_y))
old_sand_particles.append(info_append)

info_append = "(300, 90)0"
pygame.draw.rect(WIN, sand_colour, (300, 90, particle_size_x, particle_size_y))
old_sand_particles.append(info_append)

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
    mouse_cursor()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
            pygame.quit()



sys.exit()
