
from pygame.sprite import Sprite
from dino_runner.utils.constants import HEART

class Life(Sprite):
    def __init__(self):
        self.image = HEART  # importar la imagen
        self.rect = self.image.get_rect()  # para dibujarlo en el rectangulo
        self.rect.x = 25
        self.rect.y = 10
    def coordinates(self, lives):
        self.rect.x += 25  # sumar 25 para que este a lado
        if self.rect.x == 25 + 25 * lives:  # si llega a el nro de corazones,vuelve a imprimir desde el inicio para que se quede quieto en un solo lugar
            self.rect.x = 25
    def draw(self, screen):
        screen.blit(self.image, self.rect)  # dibuja los corazones
