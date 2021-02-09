import pygame
from Scene import Scene
from ship import Ship
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.ship = Ship(app)
        super().__init__('PlayScene')
        
        

    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            elif event.key == pygame.K_LEFT:
                self.ship.speed = -3
                print('se presiono una tecla')
            elif event.key == pygame.K_RIGHT:
                self.ship.speed = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.ship.speed = 0
            elif event.key == pygame.K_RIGHT:
                self.ship.speed = 0
            
            
    
    def update(self):
        self.ship.update()
        if self.ship.rect.x > self.app.width - self.ship.rect.width:
            self.ship.rect.x = self.app.width - self.ship.rect.width
        elif self.ship.rect.x < 0:
            self.ship.rect.x = 0
    
    def draw(self):
        self.screen.fill((255,255,255))
        #pygame.draw.rect(self.screen, (0, 255, 0), (0,550,self.app.width,50))
        self.ship.draw()
        

    
    def exit(self):
        print('termina: ', self.name)

    
        
