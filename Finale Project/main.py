import pygame
import random
import time

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Side Scroller")

def menu():
    image = pygame.image.load('assets\menu.png')
    image = pygame.transform.scale(image, (640,480))
    while True:
        screen.blit(image, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300, 325) and event.pos[1] in range(200, 228):
                    game()
menu()

def game():
    #background variables
    image = pygame.image.load('assets\level1.png')
    image = pygame.transform.scale(image, (640,480))
    bgx = 0

    #player variables
    player = pygame.image.load('assets/boy.png')
    player = pygame.trasnform.rotozoom(player, 0, 0.2)
    player_j = 325
    jump = 0
    gravity = 1
    jump_count = 0 

    #obstical variables
    crate = pygame.image.load('assets\crate.png')
    crate = pygame.transform.rotozoom(crate, 0, 0.8)
    crate_x = 700
    crate_speed = 2
    
    while True:
        #create background, allows for smooth 
        screen.blit(image, (bgx - 640,0))
        screen.blit(image, (0,0))
        screen.blit(image, (bgx + 640,0))

        bgx = bgx - 1
        if bgx <= -640:
            bgx = 0

        p_coll_box = screen.blit(player, (50, 325))
        if player_j < 325:
            player_j += gravity
        if jump == 1:
            player_j = player_j - 4
            jump_count += 1
            if jump_count > 40:
                jump_count = 0
                jump = 0

        c_coll_box= screen.blit(crate,(crate_x, 360))
        crate_x -= crate_speed
        if crate_x < - 50:
            crate_x == random.randint(700, 800)
            crate_speed == random.randint(2, 5)

        if p_coll_box.colliderect(c_coll_box):
            crate_speed = 0
            player = pygame.transform.rotozoom(player, 90, 0)
            time.sleep(4)
            end = pygame.image.load('assets\gameover.png')
            screen.blit(end, (0, 0))
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('scores')
            
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return menu()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:   
                jump = 1
menu()

