import pygame, math, sys, itertools

class TimeClass:
    def __init__(self, fps):
        self.clock = pygame.time.Clock()
        self.deltaTime = self.clock.tick(fps) / 1000
        self.fps = fps

    def update(self):
        # ajamuut sekundites
        self.deltaTime = self.clock.tick(self.fps) / 1000

class Vector2:
    def __init__(self, x, y):
        self.value = [x, y]
        self.x = x
        self.y = y

    def multiplyFloat(self, float):
        # korrutab numbriga läbi
        product = Vector2(self.x * float, self.y * float)
        return product

    def divideFloat(self, float):
        # jagab numbriga läbi
        quotient = Vector2(self.x / float, self.y / float)
        return quotient

    def addVector(self, Vector):
        sum = Vector2(self.x + Vector.x, self.y + Vector.y)
        return sum

    def subtractVector(self, Vector):
        difference = Vector2(self.x - Vector.x, self.y - Vector.y)
        return difference

    def roundVector(self):
        rounded = Vector2(round(self.x), round(self.y))
        return rounded

class Particle:
    def __init__(self, PosVec, SpeedVec):
        # võtab parameetriteks kaks Vector2 objecti

        self.pos = PosVec
        self.speed = SpeedVec
        self.mass = 1
        self.color = (255, 255, 255)

        # osakese raadius
        self.size = 10

    def update(self, screen):
        self.pos = self.pos.addVector(self.speed.multiplyFloat(0.1))

        pygame.draw.circle(screen, self.color, self.pos.roundVector().value, self.size, 0)

def update_list(updatable, screen):
    for i in range(len(updatable)):
        updatable[i].update(screen)

def GameLoop():
    screenWidth, screenHeight = 800, 600
    fps = 50

    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Particle system")

    screen.fill((250, 250, 250))

    #Object aja funktsioonide jaoks
    Time = TimeClass(fps)

    particle_list = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            particle_list.append(Particle(Vector2(400, 300), Vector2(i, j)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((250, 250, 250))

        update_list(particle_list, screen)

        pygame.draw.circle(screen, (255, 255, 255), (400, 400), 5, 0)
        screen.fill((255, 255, 255), (50, 50, 10, 10))

        Time.update()

if __name__ == '__main__':
    GameLoop()