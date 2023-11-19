import pygame
from random import choice
from pygame.locals import *

width =400
height =600
fps = 30


# color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue=(0,0,255)

pygame.init()
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('flappy box')
clock = pygame.time.Clock()

# Game variable
gravitasi = 0
score = 0
post_list = [[-300, 350],[-400, 250],[-200, 450],[-450, 150],[-50, 550]]

def create_pipa():
    y_pos = choice(post_list)
    p1 = Top(y_pos[0])
    p2 = Bottom(y_pos[1])
    detection =detectionpoint(p2.rect.x,y_pos[1])
    Pipas.add(p1)
    Pipas.add(p2)
    all_sprites.add(p1)
    all_sprites.add(p2)
    detect_group.add(detection)
    all_sprites.add(detection)

def show_text(text,font_size,font_color, x,y):
    font = pygame.font.SysFont(None, font_size)
    font_surface = font.render(text,True,font_color)
    screen.blit(font_surface,(x,y))
    

class box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((20,20))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = height // 2

class pipa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((20,500))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = width + 10

    def update(self):
        self.rect.x -= 4

        if self.rect.x < -20:
            self.kill()


class Top(pipa):
    def __init__(self, y):
        super().__init__()
        self.rect.y = y
    
class Bottom(pipa):
    def __init__(self, y):
        super().__init__()
        self.rect.y = y
    
class detectionpoint(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.Surface((20,120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.hit = False
    
    def update(self):
        self.rect.x -= 4

        if self.rect.x < -20:
            self.kill()


all_sprites = pygame.sprite.Group()
Pipas = pygame.sprite.Group()
detect_group = pygame.sprite.Group()
Box = box()
   
create_pipa()
all_sprites.add(Box)

# game loop
run = True

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT :
            run = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                gravitasi = 0
                gravitasi -= 5
    

    gravitasi += 0.25
    Box.rect.y += gravitasi

    box_point = pygame.sprite.spritecollide(Box,detect_group,False)
    if box_point and not box_point[0].hit:
        score += 1
        box_point[0].hit = True

    if len(Pipas) <= 0:
        create_pipa()

    all_sprites.update()
    screen.fill(black)
    all_sprites.draw(screen)
    show_text(str(score), 32 , white , width//2 ,height//4 - 100)
    pygame.display.flip()

pygame.quit()
