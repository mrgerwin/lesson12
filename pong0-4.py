import pygame as pygame
import sys as sys

def moveBall():
    global white, location, radius, thickness, black, ScreenSize, speedx, speedy, ballRect
    """
    Moves the ball when it bounces it just mirrors the direction, does not alter magnitude of speed vector
    Currently it bounces off of all 4 walls
    """
    
    #Changes the direction of the ball if it hits the left or right side of screen
    if location[0] + radius >= ScreenSize[0] or location[0] - radius <= 0: 
        speedx = -speedx
    #Changes the direction of the ball if it hits the top or bottom of the screen
    if location[1] + radius >= ScreenSize[1] or location[1] - radius <= 0:
        speedy = -speedy
    
    #Update Position
    location[0] = location[0] + speedx
    ballRect = ballRect.move(speedx, 0)
    location[1] = location[1] + speedy
    ballRect = ballRect.move(0, speedy)
    
    #Delete old circle, draw new circle, update display
    pygame.draw.circle(window, white, location, radius, thickness)
    pygame.display.flip()

def movePaddleA():
    """
    Draw the paddle on the left side of the screen
    """
    global white, padA, ScreenSize, aSpeed
    if padA.bottom >= ScreenSize[1] and aSpeed > 0:
        aSpeed = 0
    if padA.top <= 0 and aSpeed < 0:
        aSpeed = 0
    padA = padA.move(0, aSpeed)
    pygame.draw.rect(window, white, padA)

def movePaddleB():
    """
    Draw the paddle on the right side of the screen
    """
    global white, padB, ScreenSize, bSpeed
    if padB.bottom >= ScreenSize[1] and bSpeed >0:
        bSpeed =0
    if padB.top <= 0 and bSpeed <0:
        bSpeed = 0
    padB = padB.move(0, bSpeed)
    pygame.draw.rect(window, white, padB)

def collide(rect1, rect2):
    """
    Tests if the ball and paddle collide
    """
    if (rect1.colliderect(rect2)):
        print("Collide")

"""
Variables
"""

fps = 60

speedx = 1
speedy = 1
black = (0, 0, 0)
thickness = 0
radius = 20
location = [400, 400]
ballRect = pygame.Rect((location[0]-radius, location[1]-radius), (radius *2, radius *2))
white = (255, 255, 255)
ScreenSize = (1000, 600)
timer = pygame.time.Clock()
window = pygame.display.set_mode(ScreenSize)
padA = pygame.Rect((0,0), (20, 100))
padB = pygame.Rect((ScreenSize[0]-20, 0), (20,100))
aSpeed = 0
bSpeed = 0

"""
Main Loop
"""
quit = False
while quit == False:
    """Events
    """
    #Get events from event queue and iterate through each event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit = True
          pygame.quit()
          sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                aSpeed = -2
            elif event.key == pygame.K_DOWN:
                aSpeed = 2
            elif event.key == pygame.K_KP8:
                bSpeed = -2
            elif event.key == pygame.K_KP2:
                bSpeed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                aSpeed = 0
            elif event.key ==pygame.K_KP8 or event.key == pygame.K_KP2:
                bSpeed = 0
    #Check to see if it is a keyboard event or a quit event
    #if a quit event end the loop and quit pygame
    #if a keyboard event, which one was it, move the paddle that direction
    movePaddleA()
    movePaddleB()
    moveBall()
    collide(ballRect, padA)
    collide(ballRect, padB)
    window.fill(black)
    timer.tick(fps)