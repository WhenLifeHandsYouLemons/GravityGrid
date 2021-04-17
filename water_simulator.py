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
bg_colour = 255, 255, 255
window_height = 645
window_width = 1250
WIN = pygame.display.set_mode((window_width, window_height))
WIN.fill(bg_colour)

"""
VARIABLES
"""


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

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
            pygame.quit()



sys.exit()
