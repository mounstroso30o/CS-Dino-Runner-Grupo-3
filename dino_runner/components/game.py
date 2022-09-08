from tkinter.font import Font
import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

        self.running =  False
        self.score = 0
        self.death_count = 0
        self.last_score= 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                self.reset_game()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
    def events(self):
        for event in pygame.event.get(): # nos devuelve una lista de eventos 
            if event.type == pygame.QUIT: #quit es de tipo entero y es una constante q ua no se este jugando
                self.playing = False 
                self.running = False
            
    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5 
        
    def draw(self):
        self.clock.tick(FPS) # numero de actualizaciones por segundo 
        self.screen.fill((255, 255, 255)) #screen es la ventana fill es para el color 
        self.draw_background() 
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width() 
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg)) # blit es el que va hacer el trabajo pero hay que mandar una orden para hacerlo
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect) #revisar esto y corregirlo

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                self.run()
    def show_menu(self):
        
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Press any key to start", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)#####mostrar numero de muertes 
        else:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("You are died", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
            
            text = text = font.render("Score: "+str(self.last_score), True, (0, 0, 0))
            text_rect.center = (half_screen_width, half_screen_height+50)
            self.screen.blit(text, text_rect)

            text = text = font.render("Number of deaths: "+str(self.death_count), True, (0, 0, 0))
            text_rect.center = (half_screen_width, half_screen_height+100)
            self.screen.blit(text, text_rect)

        self.screen.blit(ICON,(half_screen_width - 20, half_screen_height - 140))

        pygame.display.update() #para que dibuje lo que quiero dibujar
        self.handle_events_on_menu()
    def reset_game(self):
        self.game_speed=20