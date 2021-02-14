import pygame
from Scene import Scene
from ship import Ship
from bullet import Bullet
from fleet import Alien_fleet
from alien import Alien
from score import Score
from power_up import PowerUp
import random

class PlayScene (Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.ship = Ship(app)
        self.alien_fleet = Alien_fleet(self)
        self.score = Score(app)
        self.power = PowerUp(app)
        super().__init__('PlayScene')
        
    def start(self):
        
        print('se inicia: ', self.name)
    
    
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pass
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
        self.collisions()
        self.score.update()
        self.power.update()
        
    
    def draw(self):
        self.screen.fill((255,255,255))
        self.score.draw()
        #pygame.draw.rect(self.screen, (0, 255, 0), (0,550,self.app.width,50))
        self.ship.draw()
        self.alien_fleet.draw()
        self.power.draw()
        

    
    def exit(self):
        print('termina: ', self.name)

    
    def collisions(self):
        for bullet in self.ship.weapon.bullets:
            for alien in self.alien_fleet.aliens:
                if bullet.is_active == True:
                    if(bullet.rect.x < alien.x + alien.rect.width and 
                    bullet.rect.x > alien.rect.x - alien.rect.width and
                    bullet.rect.y < alien.rect.y + alien.rect.height and
                    bullet.rect.y > alien.rect.y - alien.rect.height):
                        bullet.is_active = False
                        self.alien_fleet.aliens.remove(alien)
                        self.score.score += 1
                        if random.random() > 0.9:
                            self.power.is_active = True
                            self.power.rect.x = alien.rect.x
                            self.power.rect.y = alien.rect.y
                            self.power.addPower()

            if not self.alien_fleet.aliens:
                bullet.is_active = False

        if not self.alien_fleet.aliens:
            print ("ya no hay")
            self.alien_fleet.create_fleet()
            self.score.score = 0
            

    
        
