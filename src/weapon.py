import pygame
from bullet import Bullet

class Weapon:
    def __init__(self):
        
        self.bullets = []
        self.count = 20
        self.bullet_sprite = pygame.image.load("assets/images/bala_buena.png")    
        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shoot_sound.wav")
            
    
    def add_bullet(self):
        for i in range (self.count):
            bullet = Bullet(self.bullet_sprite)
            self.bullets.append(bullet)

    def update(self):
        for bullet in self.bullets:
            bullet.update()

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def shoot(self, x, y):
        self.add_bullet()        
        for bullet in self.bullets:
            if bullet.is_active == False:
                pygame.mixer.Sound.play(self.shoot_sound)
                bullet.rect.x = x
                bullet.rect.y = y
                bullet.is_active = True
                print(self.count)
                return

    
