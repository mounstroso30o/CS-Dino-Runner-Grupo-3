
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0 
        self.count = 0
        super().__init__(BIRD, self.type)#iniciaos nuestra clase padre 
        self.rect.y = 250
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        self.obstacle_show = BIRD[0] if self.count <10 else BIRD[1]
        self.count +=1
        if(self.count>=20):
            self.count = 0
        if(self.rect.x < -self.rect.width):
            obstacles.pop()
        
 