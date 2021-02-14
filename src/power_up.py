import pygame

class PowerUp:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/power_up.png")
        self.rect = self.image.get_rect()
        self.speed = 2
        self.is_active = False
        self.power_ups = []
        self.count = 4

    def draw(self):
        for self in self.power_ups:
            self.screen.blit(self.image, self.rect)

    def update(self):
        for self in self.power_ups:
            self.rect.y += self.speed
            if self.rect.y < 0:
                self.is_active = False

    def addPower(self):
        
        self.power_ups.append(self)