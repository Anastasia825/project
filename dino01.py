import pygame
import random

pygame.init()

color = (255,255,255)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
FPS = 20
dino = pygame.Rect(50,300,50,50) 
jamp = False
velocity = 0

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('game')

cactus = []

spawn_timer = 0

game_over = False

while True:
    canvas.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not jamp and not game_over:
                jamp = True
                velocity = -15
            elif game_over:                                             
                dino.y = 300
                jamp = False
                velocity = 0
                cactus = []
                game_over = False
    if jamp:
        dino.y += velocity
        velocity += 1
        if dino.y >= 300:
            dino.y = 300
            jamp = False

    spawn_timer += 1
    if spawn_timer > 90:
        new_cactus = pygame.Rect(800,320,20,30)
        cactus.append(new_cactus)
        spawn_timer = 0
    for new_cactus in cactus[:]:                                         
        new_cactus.x -= 5
        if new_cactus.right < 0:
            cactus.remove(new_cactus)
        if dino.colliderect(new_cactus):
            game_over = True
    pygame.draw.rect(canvas,(0,0,0),dino)
    
    for new_cactus in cactus:
        pygame.draw.rect(canvas,(34,139,34),new_cactus)
    if game_over:
        font = pygame.font.SysFont(None, 48, bold = False, italic=False)
        text = font.render('Game over', True, (200,0,0))
        canvas.blit(text,(300,150))

    pygame.display.update()
    clock.tick(60)


