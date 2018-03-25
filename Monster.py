import pygame, math, sys

pygame.init()

## Define some stuff:

display_width = 1000
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The dude and the Monster')

black = (0,0,0)
white = (255,255,255)

increment = 10
dude_width = 100
dude_height = 100
monster_width = 100
monster_height = 100

clock = pygame.time.Clock()
dudeImg = pygame.image.load('Dude.png')
monsterImg = pygame.image.load('Monster.png')

def dude(x,y):
    gameDisplay.blit(dudeImg, (x,y))

def monster(xd, yd):
    gameDisplay.blit(monsterImg, (x,y))

def game_loop():

    x = (display_width * 0.20)
    y = (display_height * 0.20)
    xd = (display_width * 0.8)
    yd = (display_width * 0.8)
    x_change = 0
    y_change = 0
    xd_change = 0
    yd_change = 0

    while 1:
        clock.tick(60)

        ## First implement player movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if not hasattr(event, 'key'): continue
            #######################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -increment
                elif event.key == pygame.K_RIGHT:
                    x_change = increment
                elif event.key == pygame.K_UP:
                    y_change = -increment
                elif event.key == pygame.K_DOWN:
                    y_change = increment
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            ########################
            print(x,y)
            keyPress = pygame.key.get_pressed()
        if x < 0 + increment*2 and keyPress[pygame.K_LEFT]:
            x_change = 0    
        elif x > display_width - dude_width - increment*2 and keyPress[pygame.K_RIGHT]:
            x_change = 0
        if y < 0 + increment*2 and keyPress[pygame.K_UP]:
            y_change = 0
        elif y > display_height - dude_height - increment * 2 and keyPress[pygame.K_DOWN]:
            y_change = 0
            
        x += x_change
        y += y_change
        
        gameDisplay.fill(white)
        dude(x,y)
        pygame.display.update()

        ## Now for the monster AI
        ## Create a predifined list with the four different actions
        ## Iterate over the list and calculate the square distance to player for each action
        ## Use argmin to get index of smallest distance
        ## Use index to take that action
        

game_loop()    

