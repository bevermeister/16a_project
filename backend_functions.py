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
    result_check_word.sort()
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

