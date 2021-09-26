# This is a Star Hero.
import pygame
import random
import math

# initialize Pygame
pygame.init()

# create game window
screen = pygame.display.set_mode((600, 500))

# Title and Icon
pygame.display.set_caption("The Guardian Angel")
icon = pygame.image.load('img/angel.png')
pygame.display.set_icon(icon)

# Hero
heroImg = pygame.image.load('img/superhero.png')
heroX = 150
heroY = 350
heroX_change = 0
heroY_change = 0
health_hero = 40

# Orc
orcImg = pygame.image.load('img/orc.png')
orcX = random.randint(0, 400)
orcY = random.randint(50, 150)
orcX_change = 0.01
orcY_change = 30
health_Orc = 7


# Dragon
dragonImg = pygame.image.load('img/dragon.png')
dragonX = random.randint(0, 400)
dragonY = random.randint(50, 200)
dragonX_change = 0.01
dragonY_change = 0
health_Dragon = 20

# fireball:
# ready- you can't see the fire on screen
# fire- the fire is in moving state
fireballImg = pygame.image.load('img/fireball.png')
fireball_X = 0
fireball_Y = 350
fireballX_change = 0
fireballY_change = 0.1
fireball_state = "ready"

def player(x,y):
    screen.blit(heroImg, (heroX, heroY))

def orc(x,y):
    screen.blit(orcImg, (orcX, orcY))

def dragon(x,y):
    screen.blit(dragonImg, (dragonX, dragonY))

def fire_fireball(x,y):
    global fireball_state
    fireball_state ="fire"
    screen.blit(fireballImg, (x, y))

def isCollision_Orc(orcX, orcY, fireball_X, fireball_Y):
    distance = math.sqrt((math.pow(orcX - fireball_X, 2))+ (math.pow(orcY- fireball_Y, 2)))
    if distance < 27:
        return True
    else:
        return False
def isCollision_Dragon(dragonX, dragonY, fireball_X, fireball_Y):
    distance = math.sqrt((math.pow(dragonX - fireball_X, 2))+ (math.pow(dragonY- fireball_Y, 2)))
    if distance < 40:
        return True
    else:
        return False


# Game loop and window close by quiting
running = True
while running:
    # changing background color Red, Green,Blue
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               # print("Left arrow is pressed")
                heroX_change = -0.1
            if event.key == pygame.K_RIGHT:
                # print("Right arrow is pressed")
                heroX_change = 0.1
            if event.key == pygame.K_SPACE:
                if fireball_state is "ready":
                    # get x coordinate of Hero to fireball
                    fireball_X = heroX
                    fireball_Y = heroY
                    fire_fireball(fireball_X, fireball_Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Keystrokes have been released")
                heroX_change = 0

    # checking for boundaries of Hero
    heroX += heroX_change
    if heroX <= 0:
        heroX = 0
    elif heroX >= 520:
        heroX = 520

    # checking movement of Orc
    orcX += orcX_change

    if orcX <= 0:
        orcX_change = 0.1
        orcY += orcX_change
    elif orcX >= 520:
        orcX_change = -0.1
        orcY += orcX_change

    # checking movement of Dragon
    dragonX += dragonX_change

    if dragonX <= 0:
        dragonX_change = 0.01
        dragonY += dragonX_change
    elif dragonX >= 520:
        dragonX_change = -0.01
        dragonY += dragonX_change

    # fireball movement
    if fireball_Y <= 0:
        fireball_Y = 520
        fireball_state = "ready"
    if fireball_state is "fire":
        fire_fireball(fireball_X, fireball_Y)
        fireball_Y -= fireballY_change

    # Collision Orc
    collision = isCollision_Orc(orcX, orcY, fireball_X, fireball_Y)
    if collision:
        fireball_Y = 500
        fireball_state = "ready"
        health_Orc -= 1
        print("Orc health ", health_Orc)

    # Collision Dragon
    collision = isCollision_Dragon(dragonX, dragonY, fireball_X, fireball_Y)
    if collision:
        fireball_Y = 500
        fireball_state = "ready"
        health_Dragon -= 1
        print("Dragon health", health_Dragon)


    # player is always visible
    player(heroX, heroY)
    orc(orcX, orcY)
    dragon(dragonX, dragonY)
    pygame.display.update()


