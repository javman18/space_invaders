import pygame
from pygame.sprite import Sprite

class Alien():
    def __init__(self, fleet, x, y):
        self.screen = fleet.app.screen
        self.image = pygame.image.load ("assets/images/ovni_bien.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 1
        self.drop_speed = 0.1

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, direction):
        self.x += (self.speed * direction)
        self.y += self.drop_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    


