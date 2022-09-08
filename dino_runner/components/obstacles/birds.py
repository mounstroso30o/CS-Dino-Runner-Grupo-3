
from dino_runner.components.obstacles.obstacle import Obstacle

class Birds(Obstacle):
    def __init__(self, image):
        self.type = 0 #
        super().__init__(image, self.type)#iniciaos nuestra clase padre 
        self.rect.y = 250
    
 