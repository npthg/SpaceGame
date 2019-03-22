import arcade.key
from random import randint

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
    def hit(self, other, hitSize):
        return (abs(self.x - other.x) <= hitSize) and (abs(self.y - other.y) <= hitSize)

class Gold(Model):
    def __init__(self, world, x, y):
       super().__init__(world, x, y, 0)

    def randomLocation(self):
        self.x = randint(0, self.world.width-1)
        self.y = randint(0, self.world.height-1)

class Ship(Model):
    DIR_HOR = 0
    DIR_VIR = 1
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.direction = Ship.DIR_VIR

    def switchDirection(self):
        if(self.direction == Ship.DIR_HOR):
            self.direction = Ship.DIR_VIR
            self.angle = 0
        else:
            self.direction = Ship.DIR_HOR
            self.angle = -90

    def update(self, delta):
        if(self.direction == Ship.DIR_VIR):
            if(self.y > self.world.height):
                self.y = 0
            self.y +=5
        if(self.direction == Ship.DIR_HOR):
            if(self.x > self.world.width):
                self.x = 0
            self.x += 5

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0

        self.gold = Gold(self, 400, 400)
        self.ship = Ship(self, 100, 100)

    def update(self, delta):
        self.ship.update(delta)

        if(self.ship.hit(self.gold, 15)):
            self.gold.randomLocation()
            self.score+=1


    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.SPACE):
            self.ship.switchDirection()
