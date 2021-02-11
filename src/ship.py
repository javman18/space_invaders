import pygame

class Ship:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/nave_aceptable.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 0.15
        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False

    def draw(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        self.rect.x += self.speed
        if self.speed > 0:
            self.move_right = True
            self.move_left = False
            
        elif self.speed < 0:
            self.move_left = True
            self.move_right = False
            
        if self.rect.x > self.screen_rect.width - self.rect.width + 15:
            self.rect.x = self.screen_rect.width - self.rect.width + 15
        elif self.rect.x < 0 - 15:
            self.rect.x = 0 - 15
        