from contextlib import redirect_stderr
from turtle import TurtleScreen
import pygame
import button

pygame.init()
pygame.font.init()

# setting up the window
width = 600
height = 800
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('VORDLE')

# background music
pygame.mixer.init()
L = ['fairytale.mp3', 'island.mp3', 'ittybitty.mp3', 'kawai.mp3', 'monkeys.mp3','sunshine.mp3', 'vacation.mp3', 'waltz.mp3', 'weasel.mp3']
track = random.choice(L)
pygame.mixer.music.load(track)
mixer.music.play(-1)

# window colors
black = (0,0,0)
white = (255,255,255)
gray = (150,150,150)
green = (60, 186, 84)
yellow = (244, 194, 13)
red = (219, 50, 54)
blue = (72, 133, 237)

# load button image
stats_img = pygame.image.load('stats.png').convert_alpha()
stats_button = button.Button(555, 10, stats_img, 0.5)

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

title1 = title_font.render('V', True, blue)
titleRect1 = title1.get_rect()
titleRect1.center = ((width // 2 - 78), height - 770)

title2 = title_font.render('O', True, red)
titleRect2 = title2.get_rect()
titleRect2.center = ((width // 2 - 48), height - 770)

title3 = title_font.render('R', True, yellow)
titleRect3 = title3.get_rect()
titleRect3.center = ((width // 2 - 15), height - 770)

title4 = title_font.render('D', True, blue)
titleRect4 = title4.get_rect()
titleRect4.center = ((width // 2 + 15), height - 770)

title5 = title_font.render('L', True, green)
titleRect5 = title5.get_rect()
titleRect5.center = ((width // 2 + 43), height - 770)

title6 = title_font.render('E', True, red)
titleRect6 = title6.get_rect()
titleRect6.center = ((width // 2 + 70), height - 770)

# draw game board boxes
def draw_boxes():
    global turn 
    global boxes
    for col in range(0,5):
        for row in range(0,6):
            pygame.draw.rect(screen, white, [col * 100 + 65, row * 100 + 60, 70, 70], 3)

# draw keyboard
def draw_keys1():
    global turn 
    global keys1
    for col in range(0,10):
        pygame.draw.rect(screen, gray, [col * 40 + 100, 650, 30, 40], border_radius=7)
        keys_text = game_font.render(keys1[col], True, white)
        screen.blit(keys_text, (col * 40 + 110, 662))

def draw_keys2():
    global turn 
    global keys2
    for col in range(0,9):
        pygame.draw.rect(screen, gray, [col * 40 + 120, 700, 30, 40], border_radius=7)
        keys_text = game_font.render(keys2[col], True, white)
        screen.blit(keys_text, (col * 40 + 132, 711))

def draw_keys3():
    global turn 
    global keys3
    for col in range(0,7):
        pygame.draw.rect(screen, gray, [col * 40 + 160, 750, 30, 40], border_radius=7)
        keys_text = game_font.render(keys3[col], True, white)
        screen.blit(keys_text, (col * 40 + 170, 763))

# stats button loop
def stats():
    # set up the stats window
    width = 500
    height = 400
    screen2 = pygame.display.set_mode([width, height])
    pygame.display.set_caption('STATISTICS')
    
    # statistics heading
    stats_font = pygame.font.Font('freesansbold.ttf', 20)
    stats_title = stats_font.render('STATISTICS', True, white, black)
    titleRect2 = stats_title.get_rect()
    titleRect2.center = (width // 2, height - 330)
    
    # histogram title
    hist_title = stats_font.render('GUESS DISTRIBUTION', True, white, black)
    titleRect3 = hist_title.get_rect()
    titleRect3.center = (width // 2, height - 200)
    
    # load exit image (x)
    exit_img = pygame.image.load('exit.png').convert_alpha()
    exit_button = button.Button(470, 10, exit_img, 0.5)

    running = True
    while running:
        # set up the stats screen background
        timer.tick(fps)
        screen.fill(black)
        screen2.blit(stats_title, titleRect2)
        screen2.blit(hist_title, titleRect3)
        
        # if x is pressed (*hovered over lol I need to fix this), go back to game screen (however it might reset progress, we need to test this)
        if exit_button.draw(screen2):
            game()

        # exit game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()

# game loop
def game():
    # redefine screen dimensions if user was to go to stats button (which resets the width/height dimensions)
    width = 600
    height = 800
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('VORDLE')
    
    # set up the game screen background
    running = True
    while running:
        timer.tick(fps)
        screen.fill(black)
        screen.blit(title1, titleRect1)
        screen.blit(title2, titleRect2)
        screen.blit(title3, titleRect3)
        screen.blit(title4, titleRect4)
        screen.blit(title5, titleRect5)
        screen.blit(title6, titleRect6)

        # if stats button is pressed
        if stats_button.draw(screen):
            stats()

        # draw game board
        draw_boxes()
        draw_keys1()
        draw_keys2()
        draw_keys3()

        # exit game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()
game()
