import pygame
import random

screen = pygame.display.set_mode((640,480)) #creates window 
pygame.display.set_caption("Side Scroller") #names window 

def menu():
    #displays menu
    image = pygame.image.load('assets\menu.png')
    image = pygame.transform.scale(image, (640,480))
    while True:
        screen.blit(image, (0,0)) #displays menu inside of window
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #adds continue if mouse is clicked in window
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

    #make font and score variables
    font = pygame.font.SysFont('comicsans', 80)
    score_counter = 0
    prev_score = 0
    new_score = 0
    
    while True:
        #create background, allows for smooth 
        screen.blit(image, (bgx - 640,0))
        screen.blit(image, (0,0))
        screen.blit(image, (bgx + 640,0))

        #moves background across screan
        bgx = bgx - 1
        if bgx <= -640:
            bgx = 0

        
        p_coll_box = screen.blit(player, (50, 325)) #creates a hit detection box around the player
        
        #adds the jump mechanic, adds a jump peak
        if player_j < 325:
            player_j += gravity
        if jump == 1:
            player_j = player_j - 4
            jump_count += 1
            if jump_count > 40:
                jump_count = 0
                jump = 0

        c_coll_box = screen.blit(crate,(crate_x, 360)) #creates hit detection for box
        crate_x -= crate_speed #moves the crate left by the speed 
        if crate_x < - 50:
            #randomly places a box and it's speed, creating variation
            crate_x == random.randint(700, 800)
            crate_speed == random.randint(2, 5)
            score_counter += 1
        

        if p_coll_box.colliderect(c_coll_box): #if player and crate collide
            crate_speed = 0 #crate stops
            player = pygame.transform.rotozoom(player, 90, 0) #player falls
            pygame.time.delay(100) #delay game over screen
            
            #will display (hopefully) the game over screen (hopefully) over the background
            end = pygame.image.load('assets\gameover.png')
            screen.blit(end, (0, 0))
            
            #will display (hopefully) the score the player got
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #display the highest score on screen
                    prev_score = font.render('Previous Score: ' + str(update_file()), 1, (255, 255, 255))
                    screen.blit(prev_score, (320 - prev_score.get_width()/2, 240))
                    
                    #display the current score on screen
                    new_score = font.render('Score: ' + str(score_counter), 1, (255, 255, 255))
                    screen.blit(new_score, (320 - new_score.get_width()/2, 320)) 
                    
                    pygame.display.update() #update screen         
            
            #if game is over, will send player back to menu after a mouse click
            pygame.display.update(100)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return menu()

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN and jump != 1: #will (hopefully) make it so the player can jump, but only once
                jump = 1
menu()

#uses score.txt to store the highest score
def update_file(score_counter):
    f = open('scores.txt', 'r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score_counter): #if the highest score is less then current score
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score_counter))
        file.close()

        return score_counter
    f.close()
    return last
