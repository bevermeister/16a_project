from contextlib import redirect_stderr # depending on finished product we might not need!
from turtle import TurtleScreen # depending on finished product we might not need!
import pygame
import button
import random
import display_functions # this will store dark/light mode, music manipulation, etc.
from pygame import mixer
from time import time

# initialize pygame and fonts
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

# load button images
stats_img = pygame.image.load('stats.png').convert_alpha()
stats_button = button.Button(555, 10, stats_img, 0.5)

settings_img = pygame.image.load('settings.png').convert_alpha()
settings_button = button.Button(590, 10, settings_img, 0.56)

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

# initialize font, create title (Google themed because Uno got a job at Google!)
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

# draw keyboard line by line
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

# stats button 
def stats():
    width = 500
    height = 400
    screen2 = pygame.display.set_mode([width, height])
    pygame.display.set_caption('STATISTICS')

    # statistics title
    stats_font = pygame.font.Font('freesansbold.ttf', 20)
    stats_title = stats_font.render('STATISTICS', True, white, black)
    statsRect1 = stats_title.get_rect()
    statsRect1.center = (width // 2, height - 340)

    # number of times player has played 
    small_font = pygame.font.Font('freesansbold.ttf', 12)
    stats_played = small_font.render('Played', True, white, black)
    statsRect2 = stats_played.get_rect()
    statsRect2.center = (width // 2 - 100, height - 260)

    # percentage of player's wins
    stats_wins = small_font.render('Win %', True, white, black)
    statsRect3 = stats_wins.get_rect()
    statsRect3.center = (width // 2 - 34, height - 260)

    # current streak
    stats_current = small_font.render('Current', True, white, black)
    statsRect4 = stats_current.get_rect()
    statsRect4.center = (width // 2 + 34, height - 260)
    stats_current2 = small_font.render('Streak', True, white, black)
    statsRect5 = stats_current2.get_rect()
    statsRect5.center = (width // 2 + 34, height - 248)

    # max streak
    stats_max = small_font.render('Max', True, white, black)
    statsRect6 = stats_max.get_rect()
    statsRect6.center = (width // 2 + 100, height - 260)
    stats_max2 = small_font.render('Streak', True, white, black)
    statsRect7 = stats_max2.get_rect()
    statsRect7.center = (width // 2 + 100, height - 248)

    # histogram title
    hist_title = stats_font.render('GUESS DISTRIBUTION', True, white, black)
    statsRectHist = hist_title.get_rect()
    statsRectHist.center = (width // 2, height - 200)

    # exit button
    exit_img = pygame.image.load('exit.png').convert_alpha()
    exit_button = button.Button(470, 10, exit_img, 0.5)

    running = True
    while running:
        timer.tick(fps)
        screen.fill(black)
        # show text
        screen2.blit(stats_title, statsRect1)
        screen2.blit(stats_played, statsRect2)
        screen2.blit(stats_wins, statsRect3)
        screen2.blit(stats_current, statsRect4)
        screen2.blit(stats_current2, statsRect5)
        screen2.blit(stats_max, statsRect6)
        screen2.blit(stats_max2, statsRect7)
        screen2.blit(hist_title, statsRectHist)

        # if x is pressed (*hovered over lol I need to fix this), go back to game screen (however it might reset progress, we need to test this)
        if exit_button.draw(screen2):
            game()

        # exit game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()

# settings button 
def settings():
    width = 500
    height = 400
    screen4 = pygame.display.set_mode([width, height])
    pygame.display.set_caption('SETTINGS')

    # settings title
    settings_font = pygame.font.Font('freesansbold.ttf', 20)
    settings_title = settings_font.render('SETTINGS', True, white, black)
    settingsRect1 = settings_title.get_rect()
    settingsRect1.center = (width // 2, height - 360)

    # change music volume, change song
    small_font = pygame.font.Font('freesansbold.ttf', 16)
    settings_music = small_font.render('Music', True, white, black)
    settingsRect2 = settings_music.get_rect()
    settingsRect2.center = (width - 300, height - 300)

    # change colors from black to white (dark mode default)
    settings_color = small_font.render('Dark Mode', True, white, black)
    settingsRect3 = settings_color.get_rect()
    settingsRect3.center = (width - 300, height - 200)

    # link to feedback form (https://forms.gle/5gXtiFWCRdHt44ac8)
    settings_feedback = small_font.render('Feedback', True, white, black)
    settingsRect4 = settings_feedback.get_rect()
    settingsRect4.center = (width - 300, height - 150)

    # message to the inspiration that started all of this!
    tiny_font = pygame.font.Font('freesansbold.ttf', 12)
    settings_message = tiny_font.render('We love you, Vishnu! <3 Aubrey, Annaka, & Uno', True, white, black)
    settingsRect5 = settings_message.get_rect()
    settingsRect5.center = (width // 2, height - 80)

    # exit button
    exit_img = pygame.image.load('exit.png').convert_alpha()
    exit_button = button.Button(470, 10, exit_img, 0.5)

    running = True
    while running:
        timer.tick(fps)
        screen.fill(black)
        screen4.blit(settings_title, settingsRect1)
        screen4.blit(settings_music, settingsRect2)
        screen4.blit(settings_color, settingsRect3)
        screen4.blit(settings_feedback, settingsRect4)
        screen4.blit(settings_message, settingsRect5)

        # if exit button is pressed
        if exit_button.draw(screen4):
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

    running = True
    while running:
        timer.tick(fps)
        screen.fill(black)
        # show text
        screen.blit(title1, titleRect1)
        screen.blit(title2, titleRect2)
        screen.blit(title3, titleRect3)
        screen.blit(title4, titleRect4)
        screen.blit(title5, titleRect5)
        screen.blit(title6, titleRect6)

        # if stats button is pressed
        if stats_button.draw(screen):
            stats()
    
        # if settings button is pressed
        if settings_button.draw(screen):
            settings()

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
