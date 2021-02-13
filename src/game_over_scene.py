from Scene import Scene
import pygame
import random

class GameOverScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("YOU LOSE", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)
        super().__init__('GameOverScene') 
        
  
    def start(self):
        
       
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('play')
                print('se presiono una tecla')
            

    def update(self):
        pass
        
    def draw(self):
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
       
    def exit(self):
        print('termina: ', self.name)