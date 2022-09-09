
import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import DINO_DEAD, HAMMER_TYPE, SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS, BIRD, numbers_life

class ObstacleManager:
    def __init__(self):
        self.obstacles= []
        self.lifes = numbers_life
        self.game_speed = 20
        
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
                if game.player.type == SHIELD_TYPE or game.player.type == HAMMER_TYPE:
                    self.obstacles.remove(obstacle)
                    
                elif game.lifes > 1:
                    self.obstacles.remove(obstacle)
                    game.lifes -= 1 
                else: 
                    game.playing = False
                    game.death_count += 1 
                    game.last_score = game.score
                    break
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []

