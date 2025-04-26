import pygame
import random
import os
import sys


pygame.init()
screen_size_display = (width_screen, hight_screen) = (600,150)
screen = pygame.display.set_mode((screen_size_display))
clock = pygame.time.Clock()
FPS = 60
gravity = 0.5
highest_scores = 0

font = pygame.font.SysFont(None, 36)
black = (0,0,0)
bg_color = (255, 255, 255)
w_color = (235, 235, 235)

dino = pygame.Rect(50, 300, 50, 50)
jump = False
velocity = 0

cactus = []

spawn_timer = 0

game_over = False

while True:
    screen.fill(w_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not jump and not game_over:
                jump = True
                velocity = -15
            elif game_over:
                dino.y = 300
                jump = False
                velocity = 0
                cactus = []
                highest_scores = 0
                game_over = False
    if jump:
        dino.y += velocity
        velocity += 1
        if dino.y >= 300:
            dino.y = 300
            jump = False

    spawn_timer += 1
    if spawn_timer > 90:
        new_cactus = pygame.Rect(800, 320, 20, 30)
        cactus.append(new_cactus)
        spawn_timer = 0 

    

    for new_cactus in cactus[:]:
        new_cactus.x -= 5
        if new_cactus.right < 0:
            cactus.remove(new_cactus)
        if dino.colliderect(new_cactus):
            game_over = True
    pygame.draw.rect(screen, black, dino)
    if not game_over:
        highest_scores += 1
    for new_cactus in cactus:
        pygame.draw.rect(screen, (34, 139, 34), new_cactus)

    score_text = font.render(f'score {highest_scores}',True, black)
    screen.blit(score_text,(10,10))
    if game_over:
        font = pygame.font.SysFont(None, 48, bold=False, italic=False)
        text = font.render("Game Over", True, (200, 0 ,0))
        screen.blit(text, (300, 150))
    pygame.display.update()
    clock.tick(60)



       
           