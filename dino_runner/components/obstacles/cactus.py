import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image,image2):
        self.shufle = random.randint(0,1)
        if(self.shufle == 0):
            self.type = random.randint(0, 2)
            super().__init__(image, self.type)#iniciaos nuestra clase padre 
            self.rect.y = 300
        elif(self.shufle == 1):
            self.type = random.randint(0, 2)
            super().__init__(image2, self.type)#iniciaos nuestra clase padre 
            self.rect.y = 325 
            
    

        