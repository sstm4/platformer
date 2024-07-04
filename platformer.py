import pygame, math
from sys import exit

"""
upload to github | done
make player move left and right with constant velocity | done
make the sprites
"""

pygame.init()

clock = pygame.time.Clock()

SCREENWIDTH = 800
SCREENHEIGHT = 800

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)
DARKRED = (190,0,0)
BGCOLOUR = (66,155,88)
PLAYERSIZE = 50
GRAV = 1

JUMPHEIGHT = -15

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(SCREENWIDTH // 2, SCREENHEIGHT // 2,PLAYERSIZE,PLAYERSIZE)
        self.vy = 0
        self.vx = 0
        self.on_ground = False
    
    def update(self,screen):
        self.on_ground = False
        self.vy += GRAV
        self.y += self.vy
        if self.bottom > SCREENHEIGHT:
            self.bottom = SCREENHEIGHT
            self.on_ground = True
            self.vy = 0
        pygame.draw.rect(screen,WHITE,self)
    
    def jump(self):
        if self.on_ground:
            self.vy = JUMPHEIGHT
            self.on_ground = False

player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player.left != 0:
            player.x -= 10
            if player.left < 0:
                player.left = 0
    if keys[pygame.K_d]:
        if player.right != SCREENWIDTH:
            player.x += 10
            if player.right > SCREENWIDTH:
                player.right = SCREENWIDTH
    
    screen.fill(BGCOLOUR)
    player.update(screen)
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    
    clock.tick(60)
pygame.quit
exit()