import pygame, random, math
width = 1000
height = 1000
win = pygame.display.set_mode((width, height))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
startPos = ["left", "right", "bottom", "top"]
clock = pygame.time.Clock()



class Dot:
    def __init__(self, radius, mass, type, x, y):
        self.type = type
        self.radius = radius
        self.mass = mass
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.xVel = random.randint(-10, 10)
        self.yVel = random.randint(-10, 10)
        self.distance = 0
        self.otherDots = []
        self.gravityNum = 0
        self.color = white
        self.redValue = 0
        self.blueValue = 0
        self.points = []
        # self.otherDots.remove(self)
        #print(self.otherDots)
        # if self.type != "star":
        #     if self.x == "left":
        #         self.x = 0
        #         self.y = random.randint(0, height)
        #         self.xVel = random.randint(1, 3)
        #         self.yVel = random.randint(-3, 3)
        #     elif self.x == "right":
        #         self.x = width
        #         self.y = random.randint(0, height)
        #         self.xVel = random.randint(-3, -1)
        #         self.yVel = random.randint(1, 3)
        #     elif self.x == "bottom":
        #         self.x = random.randint(0, height)
        #         self.y = height
        #         self.xVel = random.randint(-3, 3)
        #         self.yVel = random.randint(-3, -1)
        #     else:
        #         self.x = random.randint(0, height)
        #         self.y = 0
        #         self.xVel = random.randint(-3, 3)
        #         self.yVel = random.randint(1, 3)

        if self.type == "star":
            self.x = x
            self.y = y
            self.xVel = 0
            self.yVel = 0

    def move(self):
        # if self.xVel > 10:
        #     self.xVel = 10
        # if self.xVel < 1:
        #     self.xVel = 1
        # if self.yVel > 10:
        #     self.yVel = 10
        # if self.yVel < 1:
        #     self.yVel = 1

        #print(self.xVel, self.yVel)
        #if self.type != "star":

            #print("gravNum: " + str(self.gravityNum))
            #print("breka")
        trailSize = 5
        for i in range(trailSize):
            self.gravity()
            self.x += self.xVel
            self.y += self.yVel

            self.x = round(self.x)
            self.y = round(self.y)

            self.redValue = 255 - self.distance
            self.blueValue = self.distance - 255
            self.blueValue = 255 / 800 * self.distance
            self.redValue = (255 - (255 / 800) * self.distance)
            if self.redValue > 255:
                self.redValue = 255
            if self.redValue < 0:
                self.redValue = 0
            if self.blueValue > 255:
                self.blueValue = 255
            if self.blueValue < 0:
                self.blueValue = 0
            self.color = (self.redValue, 0, self.blueValue)

            self.points.append((self.color, (self.x, self.y), self.radius))

            if len(self.points) > trailSize:
                self.points.pop(0)
        #pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

        #print(len(self.points))


    def draw(self):
        for point in self.points:
            pygame.draw.circle(win, point[0], (point[1]), point[2])

    def gravity(self):
        for dot in stars:
            if dot == self:
                continue

            self.distance = self.calcDistance(dot)

            if self.distance == 0:
                continue
            # if self.distance < self.radius + dot.radius:
            #     dots.remove(self)
            #     dot.radius += 1
            #     dot.mass = dot.radius ** 2
            g = 100
            #print(self.distance)
            self.gravityNum = ((g * self.mass * dot.mass) / self.distance ** 2)

            #print('{:.3e}'.format(self.gravityNum))

            #print(self.gravityNum)
            #print(self.gravityNum)

            if self.gravityNum < 1:
                self.gravityNum = 1
            elif self.gravityNum > 2:
                self.gravityNum = 2

            #print(self.gravityNum)
            if self.x < dot.x:
                self.xVel += self.gravityNum
                #self.color = red
            elif self.x > dot.x:
                self.xVel -= self.gravityNum

                #self.color = white
            if self.y < dot.y:
                self.yVel += self.gravityNum
               # self.color = red

            elif self.y > dot.y:
                self.yVel -= self.gravityNum
                #self.color = white




    def calcDistance(self, other):
        try:

            return math.sqrt(((other.x - self.x) ** 2) + (other.y - self.y) ** 2)
        except ZeroDivisionError:

            return




dots = []
for i in range(10):
    size = random.randint(1, 3)
    dots.append(Dot(size, size ** 2,  "dot", 0, 0))
run = True

stars = []

stars.append(Dot(10, 10, "star", width / 2, height / 2))
#stars.append(Dot(10, 10, "star", 400, 400))

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            break
    win.fill(black)
    for dot in dots:

        # if dot.type != "star":
        #     dot.gravity()
        dot.move()
        dot.draw()
        for star in stars:
            star.move()
            star.draw()
    fps = clock.get_fps()
    print(fps)
    pygame.display.flip()