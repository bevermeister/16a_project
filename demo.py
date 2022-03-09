from cgitb import small
import pygame
import button
import random
import webbrowser
import display_functions # this will store dark/light mode, music manipulation, etc.
from pygame import mixer
from time import time
import math
from backend_functions import *
from checkDouble import *

# initialize pygame and fonts
pygame.init()
pygame.font.init()

# setting up the window
width = 450
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('VORDLE')
pygame.mouse.set_visible(True)
pointerImg = pygame.image.load('vishy_pointerImg.png')
pointerImg = pygame.transform.scale(pointerImg, (25,35))
pointerImg_rect = pointerImg.get_rect()
pointerImg_rect.size = (25,35)

# game variables
guess = ''
turn = 0
guess_list = []
result_list = []
result = []

# word lists
word_list = create_wordpick_array()
all_words = create_wordcheck_array(word_list)

# pick word from list
word = pick_random_word(word_list, 0.2)
print(word)

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
title_green = (60,186,84)
title_yellow = (244,194,13)
red = (219,50,54)
blue = (72,133,237)
box_green =(106,172,100)
box_yellow = (204, 180, 84)
background = (18,18,19)
dark_gray = (58,58,60)
off_white = (200,200,200)

# Vishnu confetti
Vishies = []
for q in range(100):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    Vishies.append([x, y])

vishnu_img = pygame.image.load("vishy_pointerImg.png")
vishnu_img = pygame.transform.scale(vishnu_img, (25, 25))
vishnu_confetti = vishnu_img.get_rect()
vishnu_confetti.size = (10, 10)

# load button images
stats_img = pygame.image.load('stats.png').convert_alpha()
stats_button = button.Button(416, 8, stats_img, 0.38)

settings_img = pygame.image.load('settings.png').convert_alpha()
settings_button = button.Button(442, 8, settings_img, 0.42)

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
title_font = pygame.font.Font('freesansbold.ttf', 30)
tiny_font = pygame.font.Font('freesansbold.ttf', 12)
guess_font = pg.font.Font('freesansbold.ttf', 34)
correct_font =pg.font.Font('freesansbold.ttf', 30)

title1 = title_font.render('V', True, blue)
titleRect1 = title1.get_rect()
titleRect1.center = (167, 23)

title2 = title_font.render('O', True, red)
titleRect2 = title2.get_rect()
titleRect2.center = (189, 23)

title3 = title_font.render('R', True, title_yellow)
titleRect3 = title3.get_rect()
titleRect3.center = (214, 23)

title4 = title_font.render('D', True, blue)
titleRect4 = title4.get_rect()
titleRect4.center = (236, 23)

title5 = title_font.render('L', True, title_green)
titleRect5 = title5.get_rect()
titleRect5.center = (257, 23)

title6 = title_font.render('E', True, red)
titleRect6 = title6.get_rect()
titleRect6.center = (278, 23)

# games functions
def draw_boxes():
    '''
    Draws the box grid to the screen.
    '''
    global turn 
    global boxes
    for col in range(0,5):
        for row in range(0,6):
            pygame.draw.rect(screen, white, [col * 75 + 49, row * 75 + 45, 53, 53], 2)

def draw_boxes_row(line):
    '''
    Draws a single row of boxes to the screen.
    Args: line: a list of the form range(line to draw, line to draw + 1)
    Returns: None
    '''
    for col in range(0,5):
        for row in line:
            pygame.draw.rect(screen, white, [col * 75 + 49, row * 75 + 45, 53, 53], 2)

# draw keyboard line by line
def draw_keys1():
    '''
    Draw the first line of the keyboard to the screen.
    '''
    global turn 
    global keys1
    for col in range(0,10):
        pygame.draw.rect(screen, gray, [col * 30 + 75, 488, 23, 30], border_radius=7)
        keys_text = game_font.render(keys1[col], True, white)
        screen.blit(keys_text, (col * 30 + 83, 497))

def draw_keys2():
    '''
    Draw the second line of the keyboard to the screen.
    '''
    global turn 
    global keys2
    for col in range(0,9):
        pygame.draw.rect(screen, gray, [col * 30 + 90, 525, 23, 30], border_radius=7)
        keys_text = game_font.render(keys2[col], True, white)
        screen.blit(keys_text, (col * 30 + 99, 533))

def draw_keys3():
    '''
    Draw the third line of the keyboard to the screen.
    '''
    global turn 
    global keys3
    for col in range(0,7):
        pygame.draw.rect(screen, gray, [col * 30 + 120, 563, 23, 30], border_radius=7)
        keys_text = game_font.render(keys3[col], True, white)
        screen.blit(keys_text, (col * 30 + 128, 573))

def change_box_color(color, box):
    '''
    Change the color of a single box on the screen
    Args: color: a tuple
          box: a tuple, index location of the box to be changed
    Returns: None
    '''
    pygame.draw.rect(screen, color, [box[1]*75 + 49, box[0] * 75 + 45, 53, 53])

def change_key_color(color, letter):
    '''
    Changes the color of a single key on the keyboard.
    Args: color: a tuple
          letter: a string, the letter on the key to be changed
    Returns: None
    '''
    if letter in keys1:
        for i in range(len(keys1)):
            if letter == keys1[i]:
                pygame.draw.rect(screen, color, [i*30 + 75, 488, 23, 30], border_radius = 7)
                keys_text = game_font.render(keys1[i], True, white)
                screen.blit(keys_text, (i * 30 + 83, 497))

    if letter in keys2:
        for i in range(len(keys2)):
            if letter == keys2[i]:
                pygame.draw.rect(screen, color, [i*30 + 90, 525, 23, 30], border_radius = 7)
                keys_text = game_font.render(keys2[i], True, white)
                screen.blit(keys_text, (i * 30 + 99, 533))

    if letter in keys3:
        for i in range(len(keys3)):
            if letter == keys3[i]:
                pygame.draw.rect(screen, color, [i*30 + 120, 563, 23, 30], border_radius = 7)
                keys_text = game_font.render(keys3[i], True, white)
                screen.blit(keys_text, (i * 30 + 128, 573))

def print_guess(guess, turn):
    '''
    Display the user's guess on the screen in the correct row.
    Args: guess: a string
          turn: an int. Determines which row to print the guess to
    Returns: None
    '''
    for i, letter in enumerate(guess):
        text_surface = guess_font.render(letter.upper(), True, white)
        screen.blit(text_surface,(i*75 + 63, turn*75 + 55, 53, 53))
        pygame.display.flip()

def show_result(result, turn, guess):
    '''
    Change the box and key colors to the correct color when the user submits their guess.
    Re-print guess after colors are changed.
    Args: result: a list. Determines the color to change to.
          turn: an int. Determines the row.
          guess: a string. Determines which keyboard letter to change the color of.
    Returns: None
    '''
    for i in range(len(result)):
        if result[i] == 0:
            change_box_color(dark_gray, (turn, i))
            change_key_color(dark_gray, guess[i])
            pg.display.flip()
        if result[i] == 1:
            change_box_color(box_yellow, (turn, i))
            pg.display.flip()
            change_key_color(box_yellow, guess[i])
        if result[i] == 2:
            change_box_color(box_green, (turn, i))
            pg.display.flip()
            change_key_color(box_green, guess[i])
    print_guess(guess, turn)

def screen_fill():
    '''
    Initializes the screen with background, game board, keyboard, and previous guesses/results.
    '''
    global guess_list
    global result_list

    screen.fill(background)

    # draw game board
    draw_boxes()
    draw_keys1()
    draw_keys2()
    draw_keys3()

    # display previous guesses and fill boxes
    turn_list = range(6)
    if len(guess_list) != 0:
        for i in range(len(guess_list)):
            show_result(result_list[i], turn_list[i], guess_list[i])

    # show text
    screen.blit(title1, titleRect1)
    screen.blit(title2, titleRect2)
    screen.blit(title3, titleRect3)
    screen.blit(title4, titleRect4)
    screen.blit(title5, titleRect5)
    screen.blit(title6, titleRect6)

# stats button 
def stats():
    '''
    Initializes the stats screen when the stats button is pressed.
    '''

    # initiate screen
    width = 375
    height = 300
    screen2 = pygame.display.set_mode([width, height])
    pygame.display.set_caption('STATISTICS')

    # statistics title
    stats_font = pygame.font.Font('freesansbold.ttf', 15)
    stats_title = stats_font.render('STATISTICS', True, white, background)
    statsRect1 = stats_title.get_rect()
    statsRect1.center = (width // 2, height - 255)

    # number of games played 
    display_font = pygame.font.Font('freesansbold.ttf', 30)
    small_font = pygame.font.Font('freesansbold.ttf', 9)
    stats_played = small_font.render('Played', True, white, background)
    statsRect2 = stats_played.get_rect()
    statsRect2.center = (width // 2 - 100, height - 195)
    games_played = display_font.render(str(get_number_of_games()), True, white, background)
    games_playedRect = games_played.get_rect()
    games_playedRect.center = (width // 2 - 100, height - 220)

    # percentage of player's wins
    stats_wins = small_font.render('Win %', True, white, background)
    statsRect3 = stats_wins.get_rect()
    statsRect3.center = (width // 2 - 50, height - 195)
    percent = display_font.render(str(get_win_percentage()), True, white, background)
    percentRect = percent.get_rect()
    percentRect.center = (width // 2 -50, height - 220)

    # current streak
    stats_current = small_font.render('Current', True, white, background)
    statsRect4 = stats_current.get_rect()
    statsRect4.center = (width // 2, height - 195)
    stats_current2 = small_font.render('Streak', True, white, background)
    statsRect5 = stats_current2.get_rect()
    statsRect5.center = (width // 2, height - 186)
    current_streak = display_font.render(str(get_current_streak()), True, white, background)
    current_streakRect = current_streak.get_rect()
    current_streakRect.center = (width // 2, height - 220)

    # max streak
    stats_max = small_font.render('Max', True, white, background)
    statsRect6 = stats_max.get_rect()
    statsRect6.center = (width // 2 + 50, height - 195)
    stats_max2 = small_font.render('Streak', True, white, background)
    statsRect7 = stats_max2.get_rect()
    statsRect7.center = (width // 2 + 50, height - 186)
    max_streak = display_font.render(str(get_longest_streak()), True, white, background)
    max_streakRect = max_streak.get_rect()
    max_streakRect.center = (width // 2 + 50, height - 220)

    # best/fastest time
    time_font = pygame.font.Font('freesansbold.ttf', 17)
    stats_time = small_font.render('Fastest', True, white, background)
    statsRect8 = stats_time.get_rect()
    statsRect8.center = (width // 2 + 100, height - 195)
    stats_time2 = small_font.render('Time', True, white, background)
    statsRect9 = stats_time2.get_rect()
    statsRect9.center = (width // 2 + 100, height - 186)
    fastest = time_font.render(str(get_fastest_time()), True, white, background)
    fastestRect = fastest.get_rect()
    fastestRect.center = (width // 2 + 100, height - 220)

    # histogram title
    hist_title = stats_font.render('GUESS DISTRIBUTION', True, white, background)
    statsRectHist = hist_title.get_rect()
    statsRectHist.center = (width // 2, height - 150)

    # histogram labels and locations
    hist_font = pygame.font.Font('freesansbold.ttf', 11)
    # labels
    hist_label1 = hist_font.render(str(1), True, white, background)
    hist_label2 = hist_font.render(str(2), True, white, background)
    hist_label3 = hist_font.render(str(3), True, white, background)
    hist_label4 = hist_font.render(str(4), True, white, background)
    hist_label5 = hist_font.render(str(5), True, white, background)
    hist_label6 = hist_font.render(str(6), True, white, background)
    # locations
    hist_label1Rect = hist_label1.get_rect()
    hist_label2Rect = hist_label2.get_rect()
    hist_label3Rect = hist_label3.get_rect()
    hist_label4Rect = hist_label4.get_rect()
    hist_label5Rect = hist_label5.get_rect()
    hist_label6Rect = hist_label6.get_rect()

    hist_labels = [hist_label1, hist_label2, hist_label3, hist_label4, hist_label5, hist_label6]
    hist_Rects = [hist_label1Rect, hist_label2Rect, hist_label3Rect, hist_label4Rect, hist_label5Rect, hist_label6Rect]

    # set positions for bars
    for i in range(len(hist_Rects)):
        hist_Rects[i].center = (65, (height - 130) + (20 * i))

    # get score distribution, note the max 
    dist = get_result_distribution()
    max_ = max(dist.values())
    for i in dist:
        if dist[i] == max_:
            green_hist = int(i)

    # histogram bars
    rect1 = [75, height - 138, (240 * dist['1']/int(max_)) + 10, 15]
    rect2 = [75, height - 118, (240 * dist['2']/int(max_)) + 10, 15]
    rect3 = [75, height - 98, (240 * dist['3']/int(max_)) + 10, 15]
    rect4 = [75, height - 78, (240 * dist['4']/int(max_)) + 10, 15]
    rect5 = [75, height - 58, (240 * dist['5']/int(max_)) + 10, 15]
    rect6 = [75, height - 38, (240 * dist['6']/int(max_)) + 10, 15]

    rect_dict = [rect1, rect2, rect3, rect4, rect5, rect6]

    # exit button
    exit_img = pygame.image.load('exit.png').convert_alpha()
    exit_button = button.Button(353, 8, exit_img, 0.5)

    running = True
    while running:
        screen.fill(background)
        # show stats and titles
        screen2.blit(stats_title, statsRect1)
        screen2.blit(stats_played, statsRect2)
        screen2.blit(games_played, games_playedRect)
        screen2.blit(stats_wins, statsRect3)
        screen2.blit(percent, percentRect)
        screen2.blit(stats_current, statsRect4)
        screen2.blit(stats_current2, statsRect5)
        screen2.blit(current_streak, current_streakRect)
        screen2.blit(stats_max, statsRect6)
        screen2.blit(stats_max2, statsRect7)
        screen2.blit(max_streak, max_streakRect)
        screen2.blit(stats_time, statsRect8)
        screen2.blit(stats_time2, statsRect9)
        screen2.blit(fastest, fastestRect)
        screen2.blit(hist_title, statsRectHist)

        # show histogram
        for i in range(6):
            screen2.blit(hist_labels[i], hist_Rects[i])

        for i in range(1,7):
            if green_hist == i:
                pygame.draw.rect(screen, box_green, rect_dict[i-1])
            else: pygame.draw.rect(screen, dark_gray, rect_dict[i-1])
        pygame.display.flip()

        #pointer
        pygame.mouse.set_visible(True)

        # exit game loop
        pressed = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = 1

        # if x is pressed (*hovered over lol I need to fix this), go back to game screen (however it might reset progress, we need to test this)
        if exit_button.draw(screen2,pressed):
            pygame.mouse.set_visible(True)
            game()


        pygame.display.flip()
    pygame.quit()

# settings button 
def settings():
    '''
    Initializes the settings screen when the settings button is pressed.
    '''
    width = 500
    height = 400
    screen4 = pygame.display.set_mode([width, height])
    pygame.display.set_caption('SETTINGS')

    # settings title
    settings_font = pygame.font.Font('freesansbold.ttf', 20)
    settings_title = settings_font.render('SETTINGS', True, white, background)
    settingsRect1 = settings_title.get_rect()
    settingsRect1.center = (width // 2, height - 340)

    # change music volume, change song
    small_font = pygame.font.Font('freesansbold.ttf', 16)
    settings_music = small_font.render('Sound', True, blue, background)
    settingsRect2 = settings_music.get_rect()
    settingsRect2.center = (width // 2, height - 300)

    # music on button
    music_on = tiny_font.render('Music On', True, white)
    on_button = button.Button(width - 307, height - 270, music_on, 1.0)

    # music off/mute button
    music_off = tiny_font.render('Music Off', True, white)
    off_button = button.Button(width - 222, height - 270, music_off, 1.0)

    # skip song button
    skip_song = tiny_font.render('Skip Song', True, white)
    skip_button = button.Button(width - 137, height - 270, skip_song, 1.0)

    # change colors from black to white (dark mode default)
    settings_color = small_font.render('Display', True, red, background)
    settingsRect3 = settings_color.get_rect()
    settingsRect3.center = (width // 2, height - 220)

    # dark mode button
    dark_font = tiny_font.render('Dark Mode', True, white)
    dark_button = button.Button(width // 2 - 14, height - 190, dark_font, 1.0)

    # light mode button
    light_mode = tiny_font.render('Light Mode', True, white)
    light_button = button.Button(width // 2 + 71, height - 190, light_mode, 1.0)

    # link to feedback form (https://forms.gle/5gXtiFWCRdHt44ac8)
    settings_feedback = small_font.render('Feedback', True, title_green, background)
    settingsRect4 = settings_feedback.get_rect()
    settingsRect4.center = (width // 2, height - 145)

    # feedback button
    feedback = tiny_font.render('Click here to share your questions, comments, or concerns!', True, white)
    feedback_button = button.Button(width // 2 + 175, height - 115, feedback, 1.0)

    # message to the inspiration that started all of this!
    settings_message = tiny_font.render('We love you, Vishnu! <3 Aubrey, Annaka, & Uno', True, title_yellow, background)
    settingsRect5 = settings_message.get_rect()
    settingsRect5.center = (width // 2, height - 70)

    # exit button
    exit_img = pygame.image.load('exit.png').convert_alpha()
    exit_button = button.Button(470, 10, exit_img, 0.5)

    running = True
    while running:
        timer.tick(fps)
        screen.fill(background)
        screen4.blit(settings_title, settingsRect1)
        screen4.blit(settings_music, settingsRect2)
        screen4.blit(settings_color, settingsRect3)
        screen4.blit(settings_feedback, settingsRect4)
        screen4.blit(settings_message, settingsRect5)

        # exit game loop
        pressed = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = 1

        # if exit button is pressed
        if exit_button.draw(screen4, pressed):
            pygame.mouse.set_visible(True)
            game()

        if on_button.draw(screen4, pressed):
            pygame.mixer.music.unpause()

        if off_button.draw(screen4, pressed):
            pygame.mixer.music.pause()

        if skip_button.draw(screen4, pressed):
            display_functions.change_song()
        
        if dark_button.draw(screen4, pressed):
            display_functions.dark_mode()
        
        if light_button.draw(screen4, pressed):
            display_functions.light_mode()
        
        if feedback_button.draw(screen4, pressed):
            webbrowser.open(r"https://forms.gle/5gXtiFWCRdHt44ac8")

        #pointer
        pygame.mouse.set_visible(False)
        pointerImg_rect.topleft = pygame.mouse.get_pos()
        screen.blit(pointerImg, pointerImg_rect)

        pygame.display.flip()
    pygame.quit()

# game loop
def game():
    '''
    Main game function. Called at the end of the file and when the user exits the stats or settings screen.
    '''
    global guess
    global turn
    global result

    # redefine screen dimensions if user was to go to stats button (which resets the width/height dimensions)
    width = 450
    height = 600
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('VORDLE')
    screen_fill()

    #initializing start time and font
    time_font = pygame.font.Font('freesansbold.ttf', 16)
    timer.tick(fps)
    start_time = pygame.time.get_ticks()

    # dummy variables
    correct = False
    was_wrong = False

    # start loop
    running = True
    while running:
        timer.tick(fps)

        # prevent entering the word check loop until enter is pressed
        enter = False

        # game events
        pressed = 0
        for event in pygame.event.get():

            # quit
            if event.type == pygame.QUIT:
                running = False

            # buttons
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = 1

            # typing
            if event.type == pygame.KEYDOWN:

                if was_wrong == True:
                    screen_fill()
                    was_wrong = False

                # add to guess
                if event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:
                    if len(guess) < 5:          
                        guess += event.unicode
               
                # backspace
                if event.key == pygame.K_BACKSPACE:
                    guess = guess[:-1]
                    change_box_color(background, (turn, len(guess)))
                    draw_boxes_row(range(turn, turn+1))

                # press enter to submit guess
                if event.key == pygame.K_RETURN and len(guess) == 5:
                    enter = True

        # display guess after each letter is typed
        print_guess(guess, turn)

        # check validity of guess after enter is presssed
        while enter:
            
            # if guess is a 5-letter english word
            if is_valid(guess.lower(), all_words):
                guess_list.append(guess)

                # check validity of each letter
                result = check_word(guess, word)
                result_list.append(result)
                
                # change main box colors to display result
                show_result(result, turn, guess)
                print_guess(guess, turn)

                # check for double letters, change result list so key is changed to highest result value color
                check = checkDouble(guess, result)

                check.get_count_dict()
                check.get_repeated()
                check.update_res_list()
                check.update_result()
                result = check.result

                # change key colors after updating result list
                for i in range(len(result)):
                    if result[i] == 0:
                        change_key_color(dark_gray, guess[i])
                    if result[i] == 1:
                        change_key_color(box_yellow, guess[i])
                    if result[i] == 2:
                        change_key_color(box_green, guess[i])

                # if guess is correct
                if guess.lower() == word:
                    # update score list and other stats
                    seconds = math.floor(((pygame.time.get_ticks() - start_time)/1000)%60)
                    minutes = math.floor((pygame.time.get_ticks() - start_time)/60000)
                    score = turn + 1
                    save_results(score, str(minutes)+"m:"+str(seconds)+"s")
                    enter = False

                    correct = True
                    # congratulations display
                    while correct:
                        # redefine screen
                        timer.tick(fps)

                        screen.fill(background)
                        # show text
                        screen.blit(title1, titleRect1)
                        screen.blit(title2, titleRect2)
                        screen.blit(title3, titleRect3)
                        screen.blit(title4, titleRect4)
                        screen.blit(title5, titleRect5)
                        screen.blit(title6, titleRect6)

                        # exit game loop
                        pressed = 0
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                            elif event.type == pygame.MOUSEBUTTONUP:
                                pressed = 1

                        # if stats button is pressed
                        if stats_button.draw(screen, pressed):
                            stats()
                    
                        # if settings button is pressed
                        if settings_button.draw(screen, pressed):
                            settings()

                        # draw game board
                        draw_boxes()
                        draw_keys1()
                        draw_keys2()
                        draw_keys3()

                        # print good job message
                        draw_badge_with_word(screen, "Good Job!", correct_font, 175, 75, (137,75), off_white, background)

                        # vishy confetti
                        for i in Vishies:
                            i[1] += 6
                            vishnu_confetti = vishnu_img.get_rect()
                            vishnu_confetti.center = i
                            vishnu_confetti.size = (25,25)
                            screen.blit(vishnu_img, vishnu_confetti)

                            if i[1] > 580:
                                i[1] = random.randrange(-50, -5)
                                i[0] = random.randrange(width)

                        timer.tick(600)

                        pygame.display.flip()

                # if guess is wrong
                else:
                    # reset guess and adjust game variables
                    guess = ''
                    turn += 1
                    enter = False

            # if guess isn't valid
            else:
                # display message
                draw_badge_with_word(screen, "Not in word list", correct_font, 250, 75, (100,75), off_white, background)

                # change so screen will be reset when user types
                was_wrong = True

                # reset guess and adjust games variables
                guess = ''
                enter = False
                continue
        
            if turn > 5 and guess != word: 
                # display correct word
                draw_badge_with_word(screen, word.upper(), correct_font, 150, 75, (150,75), off_white, background)
                pg.display.flip()

                # update score stats
                score = turn + 1
                save_results(score, str(minutes)+"m:"+str(seconds)+"s")

        # if stats button is pressed
        if stats_button.draw(screen, pressed):
            stats()
    
        # if settings button is pressed
        if settings_button.draw(screen, pressed):
            settings()

        #Time
        seconds = math.floor(((pygame.time.get_ticks() - start_time)/1000)%60)
        minutes = math.floor((pygame.time.get_ticks() - start_time)/60000)
        game_time = time_font.render(str(minutes)+"m:"+str(seconds)+"s",True,white,background)
        game_time_rect = game_time.get_rect()
        game_time_rect.topleft = (15,15)
        screen.blit(game_time,game_time_rect)

        pygame.display.flip()
    pygame.quit()
game()
