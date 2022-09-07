
import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.birds import Birds
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles= []
        self.step_index = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            self.type = random.randint(0, 2)
            if(self.type == 0):
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif(self.type == 1):
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif (self.type == 2):
                self.obstacles.append(Birds(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
        
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    