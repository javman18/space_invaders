import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.anim = []
        for i in range (9):
            self.image = pygame.image.load(f"assets/images/regularExplosion0{i}.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.anim.append(self.image)
        self.index = 0
        self.frame = self.anim[self.index]
        self.rect = self.frame.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        
    def update(self):
        speed = 4
        self.counter += 1
        if self.counter >= speed and self.index < len(self.anim) - 1:
            self.counter = 0
            self.index += 1
            self.frame = self.anim[self.index]
        if self.index >= len(self.anim) - 1 and self.counter >= speed:
            self.kill()
        
