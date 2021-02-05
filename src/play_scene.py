import pygame
from Scene import Scene
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('PlayScene')
        
        

    def start(self):
        self.platform.add_platform(self.plat_list)
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            
            
    
    def update(self):
        pass
    
    def draw(self):
        self.screen.fill((255,255,255))
        pygame.draw.rect(self.screen, (0, 255, 0), (0,550,self.app.width,50))
        
        

    
    def exit(self):
        print('termina: ', self.name)

    
        
