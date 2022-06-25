particle_speed = 5

old_sand_particles = []

class SandParticle:
    x = 0
    y = 0
    time = 0

    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start

    def updateParticle(self):
        self.time += 1
        self.y += self.time * particle_speed

old_sand_particles.append(SandParticle(1, 2))


print(old_sand_particles[0].y)
print(old_sand_particles[0].time)

old_sand_particles[0].updateParticle()

print(old_sand_particles[0].y)
print(old_sand_particles[0].time)

old_sand_particles[0].updateParticle()

print(old_sand_particles[0].y)
print(old_sand_particles[0].time)

old_sand_particles[0].updateParticle()

print(old_sand_particles[0].y)
print(old_sand_particles[0].time)