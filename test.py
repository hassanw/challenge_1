# 1 - Import library
#lets make a change to this file
#making another change to this file

import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load("/Users/Hassan/Documents/resources/images/dude.png")
keys = [False, False, False, False]
playerpos=[100,100]
# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, playerpos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
                keys[0]=True
                keys[1]=True
                keys[2]=True
                keys[3]=True
