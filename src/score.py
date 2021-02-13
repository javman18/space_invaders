import pygame

class Score:
    def __init__(self, app):
        
        self.screen = app.screen
        self.score = 0
    def draw(self):
        self.screen.blit(self.score_letters, self.score_rect)

    def update(self):
    
        self.font=pygame.font.Font("assets/fonts/HyliaSerif.ttf", 32)
        
        self.score_letters = self.font.render("Score : %d " % (self.score), True, (0,0,0))
        self.score_rect = self.score_letters.get_rect()
        self.score_rect.center = (100, 20)