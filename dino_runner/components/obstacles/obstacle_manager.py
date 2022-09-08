
import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles= []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            self.type = random.randint(0, 1)
            if self.type == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS,SMALL_CACTUS))
            elif self.type == 1:
                self.obstacles.append(Bird(BIRD))
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.last_score = game.score
                game.playing = False
                game.death_count += 1 
                game.score = 0
                break
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []

