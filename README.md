HOW TO PLAY
1. Start the game
2. Enter the length of the word
3. Try to guess the letters of the word attempt per attempt
4. See your current progress in the terminal and your score
5. Lose by running out of attempts or win the game
6. Another round starts in 6 seconds
7. Enter 0 if you want to exit the app
Enjoy!

PROGRAM FILES
1. The program has 4 files: words.txt, main.py, file_parser.py, game_actions.py.
2. words.txt containes all words from the English language
3. main.py has a terminal menu made as a while ask_user != 0 statement, which is creating a loop that will continue as long as the value of
ask_user is not equal to 0. Inside the loop, the user is prompted to guess a word and the game progresses until the user decides to exit the game by setting 0
4. file_parser.py has a file_reading function, which reads a file named words.txt line by line, removes the last two characters from each line (\n),
and then creates a dictionary where the keys are the lengths of the modified lines and the values are lists of the modified lines converted to uppercase.
5. game_actions.py contains the following functions:
5.1 The main function is the core function responsible for running the Hangman game. It initializes
the game by generating a random word of a specified length from the dictionary, sets the number of
attempts allowed based on the word length, and starts a loop where the player can input their
guesses. During each iteration of the loop, it checks if the user's input matches any letters in the
word. If the input is correct, it updates the displayed word with the correctly guessed letters. If
the input is incorrect, it increments the misses count and adjusts the player's score accordingly.
The game continues until the player either guesses the word correctly or runs out of attempts.
5.2 The word_randomizer function is responsible for generating a random word of a specified length
from the dictionary of words. It takes an input parameter word_length, which indicates the length
of the word to be generated.
5.3 The input_check function is responsible for validating and processing user input in the Hangman
game. If the game is not in progress, it first checks if the input is a digit. If the input is not a
digit, it prompts the user to enter a digit. Once the input is confirmed to be a digit, it checks if
the input is within the valid range of word lengths in the dictionary. If the input is greater than
the maximum word length available, it informs the user and returns 0.
5.4 The player_greeting function is responsible for displaying a welcoming message to the player at
the beginning of the Hangman game. It prints a greeting message introducing the game and prompting
the player to enter the preferred word length to start the game. It provides instructions on how to
input the word length and also mentions that entering 0 will allow the player to quit the game.
5.5 The hangman_parts function is responsible for displaying the parts of the hangman figure based on
the number of incorrect guesses made by the player. The function takes an integer parameter parts
which represents the number of incorrect guesses.
