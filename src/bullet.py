import pygame

class Bullet:
    def __init__(self, app, x, y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/bullet_kin.png")
        self.rect = self.image.get_rect()
        self.speed = 8
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, bullet_list):
        
        
        self.rect.y -= self.speed
        if (self.rect.y < 0):
            bullet_list.remove(self)
            print("eliminado")

        