import pygame

class PowerUp:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/powerUp.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect()
        self.speed = 0.1
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.is_active = False
        self.power_ups = []
        self.count = 4

    def draw(self):
        if self.is_active:
            self.screen.blit(self.image, self.rect)

    def update(self):
        if self.is_active:
            self.y += self.speed
        if self.rect.y > self.screen_rect.height:
            self.is_active = False
        self.rect.y = self.y
        self.rect.x = self.x

    def addPower(self, x, y):
        for _ in range (self.count):
            self.power_ups.append(self)
    
        for self in self.power_ups:
            if self.is_active == False:
                self.x = x
                self.y = y
                self.is_active = True
                print(self.count)
                return