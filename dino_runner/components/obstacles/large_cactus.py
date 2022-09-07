import random

from dino_runner.components.obstacles.obstacle import Obstacle

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)#iniciaos nuestra clase padre 
        self.rect.y = 300
        