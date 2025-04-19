import pygame
import sys
pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIDT = 600
FPS = 20
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ADD_NEW_FLAME_RATE = 25

cactus_img = pygame.image.load('cactus_bricks.png')
cactus_img_rect = cactus_img.get_rect()
cactus_img_rect.left = 0
fire_img = pygame.image.load('fire_bricks.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0

CLICK = pygame.time.Clock()

font = pygame.font.SysFont('forte', 20)

canvas = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIDT)
pygame.display.set_caption('Mario')

class Topscore:
    def __init__(self):
        self.high_score = 0

    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

    topscore = Tospcore()

class Dragon:
    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load('dragon_png')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = WINDOW_HEIDT/2
        self.dragon_img_rect.top = WINDOW_WIDTH
        self.up = True
        self.down = False
        
        def update(self):
            canvas.blit(self.dragon_img, self.dragon_img_rect)
            if self.dragon_img_rect.top <= cactus_img_rect.bottom:
                self.up = False
                self.down = True
            elif self.dragon_img_rect.bottom >= fire_img_rect.top:
                self.up = True
                self.down = False

            if self.up:
                self.dragon_img_rect.top -= self.dragon_velocity
            elif self.down:
                self.dragon_img_rect.top += self.dragon_velocity
