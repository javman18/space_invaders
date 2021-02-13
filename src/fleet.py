import pygame
from alien import Alien

class Alien_fleet:
    def __init__(self, game):
        self.game = game
        self.app = game.app
        self.screen = self.app.screen
        self.direction = 1
        self.drop_speed = 0.8
        self.aliens = []
        self.create_fleet()
        
    def create_fleet(self):
        for i in range(30, self.app.width - 100, 120):
            for j in range(30, int(self.app.height/2), 80):
                self.alien = Alien(self, i, j)
                self.aliens.append(self.alien)
    def draw(self):
        for alien in self.aliens:
            alien.draw()
    def update(self):
        for alien in self.aliens:
            alien.update(self.direction)
            if alien.check_edges():
                self.direction *= -1

    


    

