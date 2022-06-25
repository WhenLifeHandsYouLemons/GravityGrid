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
    "water" : [100, 100, 255],
    "sand" : [237, 201, 175]
}

window_height = 640
window_width = 720
window = pygame.display.set_mode((window_width, window_height))

# VARIABLES
particle_type = "sand"
particle_size = 10
speed = particle_size
max_speed = 60

sand_particles = []
water_particles = []

# CLASSES
class SandParticle:
    x = 0
    y = 0
    time = 0

    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start

class WaterParticle:
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

        # Check sand particle's left
        j = 0
        left_empty = True
        while j != i:
            if sand_particles[i].y + particle_size == sand_particles[j].y and sand_particles[i].x - particle_size == sand_particles[j].x:
                left_empty = False

            j += 1

        # Check sand particle's right
        j = 0
        right_empty = True
        while j != i:
            if sand_particles[i].y + particle_size == sand_particles[j].y and sand_particles[i].x + particle_size == sand_particles[j].x:
                right_empty = False

            j += 1

        # Choose (psuedo-)randomly between left and right
        if right_empty == True and left_empty == True:
            n = random.randint(0, 1)
            if n == 1:
                left_empty = False
            else:
                right_empty = False

        # Go right
        if right_empty == True and left_empty == False and down_empty == False:
            sand_particles[i].y += particle_size
            sand_particles[i].x += particle_size

        # Go left
        if left_empty == True and right_empty == False and down_empty == False:
            sand_particles[i].y += particle_size
            sand_particles[i].x -= particle_size

        i += 1

def createWaterParticle(mouse_pos):
    x = mouse_pos[0] // particle_size * particle_size
    y = mouse_pos[1] // particle_size * particle_size

    water_particles.append(WaterParticle(x, y))

def drawParticles(sand_particles, water_particles):
    for particle in sand_particles:
        pygame.draw.rect(window, colours["sand"], (particle.x, particle.y, particle_size, particle_size))

    for particle in water_particles:
        pygame.draw.rect(window, colours["water"], (particle.x, particle.y, particle_size, particle_size))

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
while running_window is True:
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_key_state = pygame.mouse.get_pressed()

    window.fill(colours["background"])

    drawParticles(sand_particles, water_particles)
    updateSandParticles()
    drawCursor(mouse_pos)

    clock.tick(24)

    pygame.display.update()

    # Optimisation check
    # print(len(sand_particles) + len(water_particles))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_window = False
            pygame.quit()
        # Change particle type
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                particle_type = "sand"
            elif event.key == pygame.K_w:
                particle_type = "water"

    # If the mouse is pressed down
    if mouse_key_state[0] is True:
        if particle_type == "sand":
            createSandParticle(mouse_pos)
        elif particle_type == "water":
            createWaterParticle(mouse_pos)

pygame.quit()
