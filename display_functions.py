#from contextlib import redirect_stderr
#from turtle import TurtleScreen
import pygame
import button
import random
import webbrowser
from pygame import mixer
from time import time

class Display:

    # change the song
    def change_song():
        # randomly select a new track
        pygame.mixer.init()
        L = ['fairytale.mp3', 'island.mp3', 'ittybitty.mp3', 'kawai.mp3', 'monkeys.mp3','sunshine.mp3', 'vacation.mp3', 'waltz.mp3', 'weasel.mp3']
        track = random.choice(L)
        pygame.mixer.music.load(track)
        mixer.music.play(-1)

    # default
    def dark_mode(): 
        # initialize pygame and fonts
        pygame.init()
        pygame.font.init()

        # setting up the window
        width = 450
        height = 600
        screen = pygame.display.set_mode([width, height])
        pygame.display.set_caption('VORDLE')

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

        # draw game board boxes
        def draw_boxes():
            turn 
            boxes
            for col in range(0,5):
                for row in range(0,6):
                    pygame.draw.rect(screen, white, [col * 75 + 49, row * 75 + 45, 53, 53], 2)

        # draw keyboard line by line
        def draw_keys1():
            turn 
            keys1
            for col in range(0,10):
                pygame.draw.rect(screen, gray, [col * 30 + 75, 488, 23, 30], border_radius=7)
                keys_text = game_font.render(keys1[col], True, white)
                screen.blit(keys_text, (col * 30 + 83, 497))

        def draw_keys2():
            turn 
            keys2
            for col in range(0,9):
                pygame.draw.rect(screen, gray, [col * 30 + 90, 525, 23, 30], border_radius=7)
                keys_text = game_font.render(keys2[col], True, white)
                screen.blit(keys_text, (col * 30 + 99, 533))

        def draw_keys3():
            turn 
            keys3
            for col in range(0,7):
                pygame.draw.rect(screen, gray, [col * 30 + 120, 563, 23, 30], border_radius=7)
                keys_text = game_font.render(keys3[col], True, white)
                screen.blit(keys_text, (col * 30 + 128, 573))

        # stats button 
        def stats():
            width = 375
            height = 300
            screen2 = pygame.display.set_mode([width, height])
            pygame.display.set_caption('STATISTICS')

            # statistics title
            stats_font = pygame.font.Font('freesansbold.ttf', 15)
            stats_title = stats_font.render('STATISTICS', True, white, black)
            statsRect1 = stats_title.get_rect()
            statsRect1.center = (width // 2, height - 255)

            # number of times player has played 
            small_font = pygame.font.Font('freesansbold.ttf', 9)
            stats_played = small_font.render('Played', True, white, black)
            statsRect2 = stats_played.get_rect()
            statsRect2.center = (width // 2 - 100, height - 195)

            # percentage of player's wins
            stats_wins = small_font.render('Win %', True, white, black)
            statsRect3 = stats_wins.get_rect()
            statsRect3.center = (width // 2 - 50, height - 195)

            # current streak
            stats_current = small_font.render('Current', True, white, black)
            statsRect4 = stats_current.get_rect()
            statsRect4.center = (width // 2, height - 195)
            stats_current2 = small_font.render('Streak', True, white, black)
            statsRect5 = stats_current2.get_rect()
            statsRect5.center = (width // 2, height - 186)

            # max streak
            stats_max = small_font.render('Max', True, white, black)
            statsRect6 = stats_max.get_rect()
            statsRect6.center = (width // 2 + 50, height - 195)
            stats_max2 = small_font.render('Streak', True, white, black)
            statsRect7 = stats_max2.get_rect()
            statsRect7.center = (width // 2 + 50, height - 186)

            # best/fastest time
            stats_time = small_font.render('Fastest', True, white, black)
            statsRect8 = stats_time.get_rect()
            statsRect8.center = (width // 2 + 100, height - 195)
            stats_time2 = small_font.render('Time', True, white, black)
            statsRect9 = stats_time2.get_rect()
            statsRect9.center = (width // 2 + 100, height - 186)

            # histogram title
            hist_title = stats_font.render('GUESS DISTRIBUTION', True, white, black)
            statsRectHist = hist_title.get_rect()
            statsRectHist.center = (width // 2, height - 150)

            # exit button
            exit_img = pygame.image.load('exit.png').convert_alpha()
            exit_button = button.Button(353, 8, exit_img, 0.5)

            running = True
            while running:
                timer.tick(fps)
                screen.fill(background)
                # show text
                screen2.blit(stats_title, statsRect1)
                screen2.blit(stats_played, statsRect2)
                screen2.blit(stats_wins, statsRect3)
                screen2.blit(stats_current, statsRect4)
                screen2.blit(stats_current2, statsRect5)
                screen2.blit(stats_max, statsRect6)
                screen2.blit(stats_max2, statsRect7)
                screen2.blit(stats_time, statsRect8)
                screen2.blit(stats_time2, statsRect9)
                screen2.blit(hist_title, statsRectHist)

                # exit game loop
                pressed = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pressed = 1

                # if x is pressed (*hovered over lol I need to fix this), go back to game screen (however it might reset progress, we need to test this)
                if exit_button.draw(screen2,pressed):
                    game()

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
            dark_mode = tiny_font.render('Dark Mode', True, white)
            dark_button = button.Button(width // 2 - 14, height - 190, dark_mode, 1.0)

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
                    game()

                if on_button.draw(screen4, pressed):
                    pygame.mixer.music.unpause()

                if off_button.draw(screen4, pressed):
                    pygame.mixer.music.pause()

                if skip_button.draw(screen4, pressed):
                    Display.change_song()
                
                if dark_button.draw(screen4, pressed):
                    dark_mode()
                
                if light_button.draw(screen4, pressed):
                    Display.light_mode()
                
                if feedback_button.draw(screen4, pressed):
                    webbrowser.open(r"https://forms.gle/5gXtiFWCRdHt44ac8")

                pygame.display.flip()
            pygame.quit()

        # game loop
        def game():
            # redefine screen dimensions if user was to go to stats button (which resets the width/height dimensions)
            width = 450
            height = 600
            screen = pygame.display.set_mode([width, height])
            pygame.display.set_caption('VORDLE')

            running = True
            while running:
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

                pygame.display.flip()
            pygame.quit()
        game()

    def light_mode():
        # initialize pygame and fonts
        pygame.init()
        pygame.font.init()

        # setting up the window
        width = 450
        height = 600
        screen = pygame.display.set_mode([width, height])
        pygame.display.set_caption('VORDLE')

        # window colors
        black = (255,255,255)
        white = (0,0,0)
        gray = (150,150,150)
        title_green = (60,186,84)
        title_yellow = (244,194,13)
        red = (219,50,54)
        blue = (72,133,237)
        box_green =(106,172,100)
        box_yellow = (204, 180, 84)
        background = (255,255,255)

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

        # draw game board boxes
        def draw_boxes():
            turn 
            boxes
            for col in range(0,5):
                for row in range(0,6):
                    pygame.draw.rect(screen, white, [col * 75 + 49, row * 75 + 45, 53, 53], 2)

        # draw keyboard line by line
        def draw_keys1():
            turn 
            keys1
            for col in range(0,10):
                pygame.draw.rect(screen, gray, [col * 30 + 75, 488, 23, 30], border_radius=7)
                keys_text = game_font.render(keys1[col], True, white)
                screen.blit(keys_text, (col * 30 + 83, 497))

        def draw_keys2():
            turn 
            keys2
            for col in range(0,9):
                pygame.draw.rect(screen, gray, [col * 30 + 90, 525, 23, 30], border_radius=7)
                keys_text = game_font.render(keys2[col], True, white)
                screen.blit(keys_text, (col * 30 + 99, 533))

        def draw_keys3():
            turn 
            keys3
            for col in range(0,7):
                pygame.draw.rect(screen, gray, [col * 30 + 120, 563, 23, 30], border_radius=7)
                keys_text = game_font.render(keys3[col], True, white)
                screen.blit(keys_text, (col * 30 + 128, 573))

        # stats button 
        def stats():
            width = 375
            height = 300
            screen2 = pygame.display.set_mode([width, height])
            pygame.display.set_caption('STATISTICS')

            # statistics title
            stats_font = pygame.font.Font('freesansbold.ttf', 15)
            stats_title = stats_font.render('STATISTICS', True, white, black)
            statsRect1 = stats_title.get_rect()
            statsRect1.center = (width // 2, height - 255)

            # number of times player has played 
            small_font = pygame.font.Font('freesansbold.ttf', 9)
            stats_played = small_font.render('Played', True, white, black)
            statsRect2 = stats_played.get_rect()
            statsRect2.center = (width // 2 - 100, height - 195)

            # percentage of player's wins
            stats_wins = small_font.render('Win %', True, white, black)
            statsRect3 = stats_wins.get_rect()
            statsRect3.center = (width // 2 - 50, height - 195)

            # current streak
            stats_current = small_font.render('Current', True, white, black)
            statsRect4 = stats_current.get_rect()
            statsRect4.center = (width // 2, height - 195)
            stats_current2 = small_font.render('Streak', True, white, black)
            statsRect5 = stats_current2.get_rect()
            statsRect5.center = (width // 2, height - 186)

            # max streak
            stats_max = small_font.render('Max', True, white, black)
            statsRect6 = stats_max.get_rect()
            statsRect6.center = (width // 2 + 50, height - 195)
            stats_max2 = small_font.render('Streak', True, white, black)
            statsRect7 = stats_max2.get_rect()
            statsRect7.center = (width // 2 + 50, height - 186)

            # best/fastest time
            stats_time = small_font.render('Fastest', True, white, black)
            statsRect8 = stats_time.get_rect()
            statsRect8.center = (width // 2 + 100, height - 195)
            stats_time2 = small_font.render('Time', True, white, black)
            statsRect9 = stats_time2.get_rect()
            statsRect9.center = (width // 2 + 100, height - 186)

            # histogram title
            hist_title = stats_font.render('GUESS DISTRIBUTION', True, white, black)
            statsRectHist = hist_title.get_rect()
            statsRectHist.center = (width // 2, height - 150)

            # exit button
            exit_img = pygame.image.load('exit.png').convert_alpha()
            exit_button = button.Button(353, 8, exit_img, 0.5)

            running = True
            while running:
                timer.tick(fps)
                screen.fill(background)
                # show text
                screen2.blit(stats_title, statsRect1)
                screen2.blit(stats_played, statsRect2)
                screen2.blit(stats_wins, statsRect3)
                screen2.blit(stats_current, statsRect4)
                screen2.blit(stats_current2, statsRect5)
                screen2.blit(stats_max, statsRect6)
                screen2.blit(stats_max2, statsRect7)
                screen2.blit(stats_time, statsRect8)
                screen2.blit(stats_time2, statsRect9)
                screen2.blit(hist_title, statsRectHist)

                # exit game loop
                pressed = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pressed = 1

                # if x is pressed (*hovered over lol I need to fix this), go back to game screen (however it might reset progress, we need to test this)
                if exit_button.draw(screen2,pressed):
                    game()

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
            dark_mode = tiny_font.render('Dark Mode', True, white)
            dark_button = button.Button(width // 2 - 14, height - 190, dark_mode, 1.0)

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
                    game()

                if on_button.draw(screen4, pressed):
                    pygame.mixer.music.unpause()

                if off_button.draw(screen4, pressed):
                    pygame.mixer.music.pause()

                if skip_button.draw(screen4, pressed):
                    Display.change_song()
                
                if dark_button.draw(screen4, pressed):
                    Display.dark_mode()
                
                if light_button.draw(screen4, pressed):
                    Display.light_mode()
                
                if feedback_button.draw(screen4, pressed):
                    webbrowser.open(r"https://forms.gle/5gXtiFWCRdHt44ac8")

                pygame.display.flip()
            pygame.quit()

        # game loop
        def game():
            # redefine screen dimensions if user was to go to stats button (which resets the width/height dimensions)
            width = 450
            height = 600
            screen = pygame.display.set_mode([width, height])
            pygame.display.set_caption('VORDLE')

            running = True
            while running:
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

                pygame.display.flip()
            pygame.quit()
        game()