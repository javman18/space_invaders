import pygame
from Scene import Scene
from ship import Ship
from bullet import Bullet
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.ship = Ship(app)
        
        super().__init__('PlayScene')
        self.bullet_list = []
        

    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            elif event.key == pygame.K_LEFT:
                self.ship.speed -= 5
                print('se presiono una tecla')
            elif event.key == pygame.K_RIGHT:
                self.ship.speed += 5
            elif event.key == pygame.K_SPACE:
                self.bullet_list.append(Bullet(self.app, self.ship.rect.x + 25, self.ship.rect.y))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.ship.speed = 0
            elif event.key == pygame.K_RIGHT:
                self.ship.speed = 0
            
            
    
    def update(self):
        self.ship.update()
        for bullet in self.bullet_list:
            bullet.update(self.bullet_list)
        
    
    def draw(self):
        self.screen.fill((255,255,255))
        #pygame.draw.rect(self.screen, (0, 255, 0), (0,550,self.app.width,50))
        self.ship.draw()
        for bullet in self.bullet_list:
            bullet.draw()
        

    
    def exit(self):
        print('termina: ', self.name)

    
        
