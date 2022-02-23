from cgi import print_directory
import pygame as pg
from pygame.locals import *
import random

#Checks the matches between the proposed word and the real word. Returning a list indicating correct ones with 2 and partially correct ones with 1. Incorrect ones are indicated with a 0. 
def check_word(proposed_word: str, real_word: str):
    #If incorrect length
    if len(proposed_word) != len(real_word):
        print("Word should be", len(real_word), "characters long, not",len(proposed_word),"characters long.")
        return
    
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

#Changes the status of the keyboard keys according to the result from a check of a proposed word
def change_key_status(buttons_dict: dict, proposed_word: str, result_check_word: list):
    for i in range(len(result_check_word)):
        buttons_dict[proposed_word[i]] = result_check_word[i]

#Saves the score to a text file
def save_results(score: int):
    with open('results.txt','a') as f:
        f.write(str(score)+"\n")
    f.close()

#Returns a dictionary with the distribution of the results
def get_results():
    scores_dict = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}
    with open('results.txt','r') as f:
        read_lines = f.readlines()
    
    #Getting rid of the \n
    read_lines = [x[0] for x in read_lines]
    for i in range(1,8):
        scores_dict[str(i)] = read_lines.count(str(i))
    return scores_dict

#Returns an array of five letter words, from which the random word is chosen.
def create_wordpick_array():
    with open('/Users/unothurfjell/Desktop/Skola/UC/Winter/16A/Random code/five_letter_words.txt') as f:
        lines = f.readlines()
    lines = [x[:-1].lower() for x in lines]
    lines.append('vishy')
    return(lines)

#Creates the array with all valid words. Adds the words in wordpick that isnt in wordcheck.
def create_wordcheck_array(wordpick):
    with open('/Users/unothurfjell/Desktop/Skola/UC/Winter/16A/Random code/all_words.txt') as f:
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

#Returns a random word from the wordpick_array. The random word will be 'vishy' with probability vishy_prob
def pick_random_word(wordpick_array,vishy_prob):
    rand_word = random.choice(wordpick_array)
    if random.random() < vishy_prob:
        rand_word = 'vishy'
    return rand_word

#Returns true if word is in the wordcheck array
def is_valid(word, wordcheck_array):
    return (word in wordcheck_array)
