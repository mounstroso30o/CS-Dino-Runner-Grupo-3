import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type # tipo de obstaculo que nos van a pasar
        self.rect = self.image[self.obstacle_type].get_rect() #obtenemor un tipo y pocisiones sobre una recta 
        self.rect.x = SCREEN_WIDTH

    def update (self, game_speed, obstacles):
        self.rect.x -= game_speed # resta de derecha a izquierda haciendo un efecto de moverse 
        if self.rect.x <- self.rect.width:#borrar el obtaculo que ya sale del cuadro de dibujo
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y))