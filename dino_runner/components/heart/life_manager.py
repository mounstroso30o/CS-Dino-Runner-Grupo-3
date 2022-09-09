from dino_runner.utils.constants import numbers_life
from dino_runner.components.heart.life import Life

class LifeManager:
    def __init__(self):
        self.life = numbers_life

    def update(self, game):
        if self.life > 0:
            self.life -= 1
        else:
            game.playing = False

    def draw(self, screen):
        self.screen=screen


