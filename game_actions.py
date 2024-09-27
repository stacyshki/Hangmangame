from random import randint
import file_parser as parser

word_dictionary = parser.file_reading()

def word_randomizer(word_length: int):
  word_position = randint(0, len(word_dictionary[word_length - 1]) - 1)
  return word_dictionary[word_length][word_position]


# The `main` function is the core function responsible for running the
# Hangman game. It initializes the game by generating a random word of a specified length from the
# dictionary, sets the number of attempts allowed based on the word length, and starts a loop where
# the player can input their guesses.
def main(user_answer, score, length_word):
  word = word_randomizer(length_word)
  attempts_allowed = len(word) // 2
  misses = 0
  right_inputs = ''
  while attempts_allowed != misses:
    if user_answer in  word:
      right_inputs += user_answer
      generating_string = ''
      
      for i in word:
        
        if i in right_inputs:
          generating_string += i
        else:
          generating_string += '_'
      
      right_inputs = generating_string
      print(right_inputs)
      score += 10
    else:
      print(right_inputs)
      misses += 1
      score -= 5
      hangman_parts(round((misses/attempts_allowed)*10))
    
    if right_inputs == word:
      return f'\nCongratulations! You guessed the word: {word.title()}\nYour score: {score}\n', score
    
    user_answer = input('\nTry to guess the letter: ').upper()
    if len(user_answer) != 1:
      print('\nYou gave more than 1 letter per time, so only the first is considered as the answer\n')
      user_answer = user_answer[0]
  
  return f'\nSorry, you ran out of guesses. The word was: {word.title()}\n Your score: {score}\n', score


def hangman_parts(parts  : int):
  hangman = [
    '----',
    '|  |',
    '|  |',
    '| ()',
    '| /|\\',
    '| /\\',
    '|',
    '|',
    '|',
    '----'
  ]
  for i in range(parts):
    print(hangman[i])


def player_greeting():
  print('\nHello!\nThis is a Hangman game!\nLet`s start!\n')
  print(f'Enter the preferred word length!\n\t1-{tuple(word_dictionary.keys())[-1]} -- can be the word length\n\tEnter 0 to quit\n')


# The `input_check` function is responsible for validating and processing user input. If the game
# is not in progress, it first checks if the input is a digit. If the input is not a digit, it
# prompts the user to enter a digit. Once the input is confirmed to be a digit, it checks if the
# input is within the valid range of word lengths in the dictionary. If the input is greater than
# the maximum word length available, it informs the user and returns 0.
def input_check(user_answer, in_game : bool, score, length_word = 0):
  if not in_game:
    
    while not user_answer.isdigit():
      user_answer = input('\nYour input must be a digit: ')
    
    user_answer = int(user_answer)
    
    if user_answer > int(tuple(word_dictionary.keys())[-1]):
        print(f'\nThere is no word of such length in the dictionary! Maximum word length is {tuple(word_dictionary.keys())[-1]}\n')
        return 0
    
    return user_answer
  
  if len(user_answer) == 1:
    return main(user_answer, score, length_word)
  
  print('\nYou gave more than 1 letter per time, so only the first is considered as the answer\n')
  return main(user_answer[0], score, length_word)
