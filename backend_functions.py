from cgi import print_directory
import pygame as pg
from pygame.locals import *
import random

"""
Checks the matches between the proposed word and the real word. Returning a list indicating correct ones with 2 and partially correct ones with 1. Incorrect ones are indicated with a 0. 

Args:
    proposed_word (str): the word that the player guessed
    real_word (str): the actual word

Returns:
    return_array (list): an array indicating the correctness of the proposed word
"""
def check_word(proposed_word: str, real_word: str):
    #If incorrect length
    if len(proposed_word) < len(real_word):
        raise ValueError('The word is too short, must be ' + str(len(real_word)) + ' characters.')
    elif len(proposed_word) > len(real_word):
        raise ValueError('The word is too long, must be ' + str(len(real_word)) + ' characters.')
    
    #Creating lists
    proposed_word = list(proposed_word.lower())
    real_word = list(real_word.lower())
    return_array = [0 for i in range(len(proposed_word))]

    # First do the correct ones
    for i in range(len(proposed_word)):
        if proposed_word[i] == real_word[i]:
            return_array[i] = 2
            #Replace the ones that were correct with a non-occurring sign
            real_word[i] = "-"
            proposed_word[i] = "%"

    # Now do the partially correct ones      
    for i in range(len(proposed_word)):
        if proposed_word[i] in real_word:
            return_array[i] = 1
            real_word[real_word.index(proposed_word[i])] = "?"
            proposed_word[i] = "="
    return return_array

"""
Changes the status of the keyboard keys according to the result from a check of a proposed word

Args:
    buttons_dict (dict): a dictionary of the keys in the keyboard to be changed
    proposed_word (str): the word that the player guessed
    result_check_word (list): the result from the check_word function
"""
def change_key_status(buttons_dict: dict, proposed_word: str, result_check_word: list):
    for i in range(len(result_check_word)):
        buttons_dict[proposed_word[i]] = result_check_word[i]

"""
Saves the score to a text file

Args:
    score (int): number of guesses needed
    proposed_word (str): the word that the player guessed
"""
def save_results(score: int, time: int):
    try:
        with open('results.txt','a') as f:
            f.write(str(score)+" "+str(time)+"\n")
        f.close()
    except OSError:
        raise OSError('Could not open/load file. Make sure that the file is in your directory.')

"""
Returns a dictionary with the distribution of the results

Returns:
    scores_dict (dict): a dictionary indicating the distribution of the scores
"""
def get_result_distribution():
    scores_dict = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    
    #Getting rid of the \n
    read_lines = [x[0] for x in read_lines]
    for i in range(1,8):
        scores_dict[str(i)] = read_lines.count(str(i))
    return scores_dict

"""
Returns the top x results

Args:
    x (int): the number of top scores needed

Returns:
    top_scores (list): the x top scores
"""
def get_top_scores(x: int):
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    read_lines = [x[:-1] for x in read_lines]
    read_lines = [x.split(" ") for x in read_lines]
    read_lines.sort()
    f.close()
    return read_lines[:x]

"""
Returns the fastest time the player has completed the game in

Returns:
    fastest_time (int): the fastest time in milliseconds. N/A if no games played.
"""
def get_fastest_time():
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    if len(read_lines) > 0:
        read_lines = [x[:-1] for x in read_lines]
        read_lines = [x.split(" ") for x in read_lines]
        read_lines.sort(key=lambda x: x[1])
        return read_lines[0][1]
    else:
        return "N/A"

"""
Returns the longest win streak

Returns:
    longest_streak (int): the longest win streak achieved so far. N/A if no games played.
"""
def get_longest_streak():
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    if len(read_lines) > 0:
        longest_streak = 0
        current_streak = 0
        read_lines = [x[:-1] for x in read_lines]
        read_lines = [x.split(" ") for x in read_lines]
        for score in read_lines:
            if int(score[0]) < 7:
               current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    current_streak = 0
        if current_streak > longest_streak:
            longest_streak = current_streak
        return longest_streak
    else:
        return "N/A"

"""
Returns the current win streak

Returns:
    current_streak (int): the current win streak. N/A if no games played.
"""
def get_current_streak():
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    if len(read_lines) > 0:
        current_streak = 0
        read_lines = [x[:-1] for x in read_lines]
        read_lines = [x.split(" ") for x in read_lines]
        for score in read_lines:
            if int(score[0]) < 7:
               current_streak += 1
            else:
                current_streak = 0
        return current_streak
    else:
        return "N/A"

"""
Returns the win percentage, expressed as percentage

Returns:
    win_percentage (int): the percentage of games won. N/A if no games played.
"""
def get_win_percentage():
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    if len(read_lines) > 0:
        no_wins = 0
        read_lines = [x[:-1] for x in read_lines]
        read_lines = [x.split(" ") for x in read_lines]
        for score in read_lines:
            if int(score[0]) < 7:
               no_wins += 1
        percentage = round(100*no_wins/len(read_lines))
        return percentage
    else:
        return "N/A"


"""
Returns the number of games played

Returns:
    no_games (int): The number of games played. N/A if no games played.
"""
def get_number_of_games():
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    if len(read_lines) > 0:
        read_lines = [x[:-1] for x in read_lines]
        read_lines = [x.split(" ") for x in read_lines]
        return len(read_lines)
    else:
        return "N/A"


"""
Returns an array of five letter words, from which the random word is chosen.

Returns:
    lines (list): A list of words from where to pick the random word
"""
def create_wordpick_array():
    with open('five_letter_words.txt') as f:
        lines = f.readlines()
    lines = [x[:-1].lower() for x in lines]
    lines.append('vishy')
    return(lines)

"""
Creates the array with all valid words. Adds the words in wordpick that isnt in wordcheck.

Returns:
    lines (list): A list of words from where to check if the word is valid
"""
def create_wordcheck_array(wordpick):
    with open('all_words.txt') as f:
        lines = f.readlines()
    lines = [x[:-1].lower() for x in lines]
    final_lines = []
    for element in lines:
        if element.isalpha() and len(element) == 5:
            final_lines.append(element)
    final_lines.append('vishy')
    for word in wordpick:
        if word not in final_lines:
            final_lines.append(word)
    return(final_lines)

"""
Returns a random word from the wordpick_array. The random word will be 'vishy' with probability vishy_prob

Returns:
    rand_word (str): The chosen random word
"""
def pick_random_word(wordpick_array,vishy_prob):
    rand_word = random.choice(wordpick_array)
    if random.random() < vishy_prob:
        rand_word = 'vishy'
    return rand_word


"""
Returns true if word is in the wordcheck array

Returns:
    in_array (bool): True if word is in wordcheck array
"""
def is_valid(word, wordcheck_array):
    return (word in wordcheck_array)
"""
Draws a small badge with the correct word

Args:
    screen (pygame screen): The screen to blit the badge onto
    correct_word (str): The correct word to show on the badge
    font_name (str): Name of font to be used
    font_size (int): Size of font
    rectangle_width (int): The width of the badge
    rectangle_height (int): The height of the rectangle
    rectangle_corner_coordinates (tuple): the coordinates of the upper left corner of the triangle
    rect_color (tuple): The background color of the rectangle in RGB-format
    text_color (tuple): The text color in RGB-format
"""
def draw_badge_with_word(screen,correct_word,font,rectangle_width,rectangle_height,rectange_corner_coordinates,rect_color,text_color):
    rect = pg.Rect(rectange_corner_coordinates,(rectangle_width,rectangle_height))
    pg.draw.rect(screen,rect_color,rect)

    (text_width,text_height) = font.size(correct_word)
    screen.blit(font.render(correct_word, True, text_color),(rectange_corner_coordinates[0]+rectangle_width/2-text_width/2,rectange_corner_coordinates[1]+rectangle_height/2-text_height/2))

