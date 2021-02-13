import pygame
from pygame.sprite import Sprite
class Bullet:
    def __init__(self, image):
        
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 8        
        self.is_active = False
    
    def update(self):
        
        if self.is_active == True:
            self.rect.y -= self.speed
        if self.rect.y < 0:
            self.is_active = False

    def draw(self, screen):
        if self.is_active:
            screen.blit(self.image, self.rect)


        