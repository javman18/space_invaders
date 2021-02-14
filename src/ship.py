import pygame
from weapon import Weapon

class Ship:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/dark_ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 0.15
        self.acceleration = 0.05
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False
        self.weapon = Weapon()



    def draw(self):
        self.weapon.draw(self.screen)
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.move_right and self.rect.x + self.rect.width - 15 < self.screen_rect.width:
            print(self.speed)
            self.x += self.speed     
        elif self.move_left and self.rect.x + 15 > 0:
            print(self.speed)
            self.x -= self.speed    
        else:
            self.speed = 4
        self.rect.x = self.x
        self.weapon.update()
    def shoot(self):
        self.weapon.shoot(self.rect.x + 25, self.rect.y)
        
        