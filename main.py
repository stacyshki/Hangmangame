import game_actions as game
from time import sleep

score = 0
game.player_greeting()
ask_user = game.input_check(input('\nSelect the preferred word length: '), False, score)

while ask_user != 0:
  guess_letter, score = game.input_check(input('\nTry to guess the letter: ').upper(), True, score, ask_user)
  print(guess_letter)
  sleep(3)
  print('\nThe game is over! It will restart in 3 seconds!\nYour score will not be removed until you exit this app!\n')
  sleep(3)
  game.player_greeting()
  ask_user = game.input_check(input('\nSelect the preferred word length: '), False, score)

print('\nThanks for using our app to play this amazing game! Looking to seeing you soon!')
