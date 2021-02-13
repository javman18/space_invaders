import pygame
from Scene import Scene
from ship import Ship
from bullet import Bullet
from fleet import Alien_fleet
from alien import Alien
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.ship = Ship(app)
        self.alien_fleet = Alien_fleet(self)
        
        super().__init__('PlayScene')
        
    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                self.app.change_scene('intro')
                print('se presiono una tecla')
            elif event.key == pygame.K_LEFT:
                self.ship.move_left = True
                print('se presiono una tecla')
            elif event.key == pygame.K_RIGHT:
                self.ship.move_right = True
            elif event.key == pygame.K_SPACE:
                self.ship.shoot()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.ship.move_left = False
            elif event.key == pygame.K_RIGHT:
                self.ship.move_right = False
            
    def update(self):
        self.ship.update()
        self.alien_fleet.update()
        self.colisions()
        
    
    def draw(self):
        self.screen.fill((255,255,255))
        #pygame.draw.rect(self.screen, (0, 255, 0), (0,550,self.app.width,50))
        self.ship.draw()
        self.alien_fleet.draw()
        

    
    def exit(self):
        print('termina: ', self.name)

    
    def colisions(self):
        for bullet in self.ship.weapon.bullets:
            for alien in self.alien_fleet.aliens:
                if bullet.is_active == True:
                    if(bullet.rect.x < alien.x + alien.rect.width and 
                    bullet.rect.x > alien.rect.x - alien.rect.width and
                    bullet.rect.y < alien.rect.y + alien.rect.height and
                    bullet.rect.y > alien.rect.y - alien.rect.height):
                        bullet.is_active = False
                        self.alien_fleet.aliens.remove(alien)


    
        
