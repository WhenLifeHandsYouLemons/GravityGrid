"""
Made by - Sooraj.S
GitHub - https://github.com/WhenLifeHandsYouLemons
Twitter - https://twitter.com/LemonsHandYou
Instagram - https://www.instagram.com/whenlifehandsyoulemons1/
Latest Release - https://github.com/WhenLifeHandsYouLemons/Particle-Simulator/releases
"""

# IMPORTS
import random
import pygame

# APP WINDOW
colours = {
    "background" : [50, 50, 50],
    "border" : [10, 10, 10],
    "cursor" : [200, 200, 200],
    "sand" : [237, 201, 175]
}

window_height = 640
window_width = 720
window = pygame.display.set_mode((window_width, window_height))

# VARIABLES
particle_size = 10
speed = particle_size
max_speed = 60

sand_particles = []

# CLASSES
class SandParticle:
    x = 0
    y = 0
    time = 0

    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start

# FUNCTIONS
def createSandParticle(mouse_pos):
    x = mouse_pos[0] // particle_size * particle_size
    y = mouse_pos[1] // particle_size * particle_size

    sand_particles.append(SandParticle(x, y))

def updateSandParticles():
    i = 0
    while i != len(sand_particles):
        # Increment particle time
        sand_particles[i].time += 1

        # Get increase of y and change y position
        y_increment = sand_particles[i].time * speed
        if y_increment > max_speed:
            y_increment = max_speed

        sand_particles[i].y += y_increment

        # Check bottom border
        if sand_particles[i].y + particle_size > window_height:
            sand_particles[i].y = window_height - particle_size

        # Check sand particle underneath
        j = 0
        down_empty = True
        while j != i:
            if sand_particles[i].y >= sand_particles[j].y and sand_particles[i].x == sand_particles[j].x:
                sand_particles[i].y = sand_particles[j].y - particle_size
                down_empty = False
            else:
                j += 1

        # Check sand particle's bottom left
        j = 0
        bottom_left_empty = True
        while j != i:
            if sand_particles[i].y + particle_size == sand_particles[j].y and sand_particles[i].x - particle_size == sand_particles[j].x:
                bottom_left_empty = False

            j += 1

        # Check sand particle's bottom right
        j = 0
        bottom_right_empty = True
        while j != i:
            if sand_particles[i].y + particle_size == sand_particles[j].y and sand_particles[i].x + particle_size == sand_particles[j].x:
                bottom_right_empty = False

            j += 1

        # Choose (psuedo-)randomly between bottom left and bottom right
        if bottom_right_empty == True and bottom_left_empty == True:
            n = random.randint(0, 1)
            if n == 1:
                bottom_left_empty = False
            else:
                bottom_right_empty = False

        # Go bottom right
        if bottom_right_empty == True and bottom_left_empty == False and down_empty == False:
            sand_particles[i].y += particle_size
            sand_particles[i].x += particle_size

        # Go bottom left
        if bottom_left_empty == True and bottom_right_empty == False and down_empty == False:
            sand_particles[i].y += particle_size
            sand_particles[i].x -= particle_size

        i += 1

def drawParticles(sand_particles):
    for particle in sand_particles:
        pygame.draw.rect(window, colours["sand"], (particle.x, particle.y, particle_size, particle_size))

def drawCursor(mouse_pos):
    x = mouse_pos[0] // particle_size * particle_size
    y = mouse_pos[1] // particle_size * particle_size

    pygame.draw.rect(window, colours["cursor"], (x+particle_size, y, particle_size, particle_size))
    pygame.draw.rect(window, colours["cursor"], (x, y+particle_size, particle_size, particle_size))
    pygame.draw.rect(window, colours["cursor"], (x-particle_size, y, particle_size, particle_size))
    pygame.draw.rect(window, colours["cursor"], (x, y-particle_size, particle_size, particle_size))

# MAIN LOOP
clock = pygame.time.Clock()

running_window = True
while running_window == True:
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_key_state = pygame.mouse.get_pressed()

    window.fill(colours["background"])

    drawParticles(sand_particles)
    updateSandParticles()
    drawCursor(mouse_pos)

    clock.tick(24)

    pygame.display.update()

    # Optimisation check
    # print(len(sand_particles))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_window = False
            pygame.quit()

    # If the mouse == pressed down
    if mouse_key_state[0] == True:
        createSandParticle(mouse_pos)

pygame.quit()
