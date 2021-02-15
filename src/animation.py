import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        
    def load_images(self):
        for i in range (9):
            img = pygame.image.load(f"assets/images/regularExplosion0{i}.png")
            img = pygame.transform.scale(img, (80, 80))
            self.images.append(img)

    def update(self):
        speed = 4
        self.counter += 1
        if self.counter >= speed and self.index < len(self.images) - 1:
            print ("explota")
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= speed:
            self.kill()
        
