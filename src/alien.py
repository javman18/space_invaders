import pygame

class Alien:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load ("assets/images/ovni_bien.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.speed = 0.1

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, direction):
        self.x += (self.speed * direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


