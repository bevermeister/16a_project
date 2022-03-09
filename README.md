# 16a_project
16A Final Project: VORDLE

Group Members: Aubrey Gilman, Annaka Schone, and Uno Thurfjell

Project Description: 
VORDLE is our own version of the popular online game Wordle, except renamed to ‘VORDLE” to pay homage to our TA, Vishnu! The basic concept of the game is that there is a random five-letter word in the system, and you have six tries to figure out the correct word. Similar concept to Mastermind, with every guess you make, the game will tell you if each letter is correct and in the right spot (green box), correct and in the wrong spot (yellow box), or incorrect and not in the word (gray. box), allowing the player to deduce what the word might be. It includes extra features in contrast to the original game, including background music, a timer, unlimited words rather than a daily word, and other fun add-ons!


Package Installation: 
For this project, we installed the Pygame package in order to develop the game. We used the latest version of Pygame, Pygame 3.9. To easily install the Pygame package, we used the PIP installation tool, and then inputted the following command in the terminal to install Pygame: pip install pygame. 


Demo File Description: 
The demo file contains our main loops and functions to play the game. In order to start the game, you must download all of the files as instructed and then run the demo file using a Python compatible software (we chose to run it using Visual Studio Code). From there, wait a moment for the game to load. You should see our main game screen that is a black, rectangular window with white boxes (6x5), a keyboard, and background music playing. Start the game by typing in your first five-letter word as a guess, and continue until you guess the word or are not able to guess it in six tries. The game only accepts valid, five-letter words as guesses. From the main screen, you have the choice to click on one of two buttons, the settings button and the stats button. The settings button allows you to change the display mode of the game (light or dark), manipulate the background music, or provide feedback to the game creators. The stats button allows you to see your playing history and your game statistics.

![Screenshot](https://github.com/bevermeister/16a_project/blob/main/screenshots/screenshot.png) ![Screenshot](https://github.com/bevermeister/16a_project/blob/main/screenshots/screenshot1.png) ![Screenshot](https://github.com/bevermeister/16a_project/blob/main/screenshots/screenshot4.png) ![Screenshot](https://github.com/bevermeister/16a_project/blob/main/screenshots/screenshot2.png) ![Screenshot](https://github.com/bevermeister/16a_project/blob/main/screenshots/screenshot3.png) 


Scope and Limitations: 
This game cannot be widespread and distributed to everyday users that cannot run python code or do not have Pygame installed. We do think that this is a fun spin on the popular game 'Wordle' and has features that would be enjoyed by more than just our class. This project illustrates how simple, generic games can be optimized and customized to have different themes and features. One limitation that we saw is that if you were to switch the display mode mid-game from light to dark or vis versa, you will lose your progress because of the way we set up our functions. However, we did not see this as a huge roadblock because we made the assumption that users would not click those buttons mid-game. Another limitation that we experienced is you need to end the program in order to restart the game, however it saves your progress for the statistics screen! As mentioned in the previous limitiation, however, if you switch display modes, it will restart the game because it is re-running the code in order to change the display colors, so that is another way to restart it. There is a slight glitch with the exit button on the stats screen because there is a lot running on that screen, however, it is still functional, so it is more of a presentation issue rather than a limitation. There are other features that we considered but ultimatelty decided to scrap in this project, including but not limited to, themes that users could select that would modify the word bacnk they are guessing from, maniupuations of the number of letters users wanted to guess from, difficulty levels being implemented, and so-on.


License and Terms of Use: MIT License
Copyright (c) [2022] [Aubrey Gilman, Annaka Schone, Uno Thurfjell]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the 
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


References and Acknowledgement: 
- Pygame documentation - https://web.archive.org/web/20220223214213/https://www.pygame.org/docs/
- NYT Wordle - https://www.nytimes.com/games/wordle/index.html

Dataset Background and Source:
- five-letter English words - https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
- all English words - https://github.com/dwyl/english-words/blob/master/words.txt


Tutorials Used:
- Game board tutorial - https://www.youtube.com/watch?v=D8mqgW0DiKk&t=1029s
  - used to set up the game board boxes and initial formatting for game loop on the main screen
  - added our own keyboard
  - added buttons to the main screen
  - added timer to main screen

- Button tutorial - https://www.youtube.com/watch?v=8SzTzvrWaAA&t=1689s
  - used to set up all of the buttons on the main, settings, and stats screens 
  - made multiple buttons with images
  - edited the press down commands for the cursor
  - edited the button class and manipulated it to work for our current project


- Snow tutorial - https://www.youtube.com/watch?v=tj01ESA4peo
  - used to make the confetti when you win
  - uploaded an image to the confetti
  - manipulated the fps/speed of the confetti
  - made it only run when the user wins a game
