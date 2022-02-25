from turtle import TurtleScreen
import pygame

pygame.init()

# setting up the window
width = 600
height = 800
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Vordle')

# window colors
black = (0,0,0)
white = (255,255,255)
gray = (211,211,211)

# initializa game board boxes
turn = 0
boxes = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]
keys1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
keys2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
keys3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

# frame rate
fps = 60
timer = pygame.time.Clock()

# initialize font, create title
game_font = pygame.font.Font('freesansbold.ttf', 15)
title_font = pygame.font.Font('freesansbold.ttf', 40)
title = title_font.render('V O R D L E', True, white, black)
titleRect = title.get_rect()

# draw game board boxes
def draw_boxes():
    global turn 
    global boxes
    for col in range(0,5):
        for row in range(0,6):
            pygame.draw.rect(screen, white, [col * 100 + 65, row * 100 + 60, 70, 70], 3, 5)

# draw keyboard
def draw_keys1():
    global turn 
    global keys1
    for col in range(0,10):
        pygame.draw.rect(screen, gray, [col * 40 + 100, 650, 30, 40], 3, 5)
        keys_text = game_font.render(keys1[col], True, white)
        screen.blit(keys_text, (col * 40 + 110, 662))

def draw_keys2():
    global turn 
    global keys2
    for col in range(0,9):
        pygame.draw.rect(screen, gray, [col * 40 + 120, 700, 30, 40], 3, 5)
        keys_text = game_font.render(keys2[col], True, white)
        screen.blit(keys_text, (col * 40 + 132, 711))

def draw_keys3():
    global turn 
    global keys3
    for col in range(0,7):
        pygame.draw.rect(screen, gray, [col * 40 + 160, 750, 30, 40], 3, 5)
        keys_text = game_font.render(keys3[col], True, white)
        screen.blit(keys_text, (col * 40 + 170, 763))
# game loop
running = True
while running:
    timer.tick(fps)
    screen.fill(black)
    screen.blit(title, titleRect)
    draw_boxes()
    draw_keys1()
    draw_keys2()
    draw_keys3()
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()

 

 