import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLSION_DISTANCE = 27

#Initalize Pygame
pygame.init()

#Create the screen
screen = pygame.display.set_model((SCREEN_WIDTH , SCREEN_HEIGHT))

#background
background = pygame.image.load
(r"")
background = pygame.transform.scale(background, (SCREEN_WIDTH , SCREEN_HEIGHT))

pygame.display.set_caption("Space Invader")
icon=pygame.image.load
(r"")
icon = pygame.transfrom.scale(icon,(64,64))
pygame.display.set_icon(icon)

playering = pygame.image.load(r"")
playering = pygame.transform.scale(playering, (64,64))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_Image=pygame.image.load(r""
    )
    enemy_Image = pygame.transform.scale(enemy_Image,(64,64))
    enemyImg.append(enemy_image)
    enemyX.append(random.randiant(0,SCREEN_WIDTH - 64 ))
    enemyY.append(random.randiant(ENEMY_START_Y_MIN , ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

    