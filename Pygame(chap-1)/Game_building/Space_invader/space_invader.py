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
screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

#background
background = pygame.image.load
(r"C:\Users\User\Desktop\Codingal\Pygame(chap-1)\Game_building\☆_𓋼𓍊 𓆏 𓍊𓋼𓍊.jpg")
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

bulletImg = pygame.image.load(r"C:\Users\User\Desktop\Codingal\Pygame(chap-1)\Game_building\background3.jpg")
bulletImg = pygame.transform.scale(bulletImg, (16,24))
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True , (255 , 255 , 255))
    screen.blit(over_text , (200, 250))

def player( x,y)
    screen.blit(playering,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16 , y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance= math.aqrt((enemyX - bulletX)** 2 +(enemyY- bulletY)**2)
    return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill(0,0,0)
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerY_change = 5
            if event.key ==pygame.K_space and bullet_state == "ready":
                bulletX =playerX
                fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT , pygame.K_EIGHT]:
            playerX_change =0

    playerX += playerX_change
    playerX = max(0,min(playerX,SCREEN_WIDTH- 64))

    for i in range(num_of_enemies):
        if enemyY[i] >340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            