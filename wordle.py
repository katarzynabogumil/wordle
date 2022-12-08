import string
import os
import random
from colorama import Fore, Back, Style

rounds = 0
displays = []
keyboard = {}


def main():
  # read allowed guesses from a dictionary
  allowed_guesses = read_guesses()

  # read allowed aswers from a dictionary
  answers = read_answers()

  # pick an answer
  answer = random.choice(answers).upper()

  # display empty squares and keyboard
  display_game()

  global rounds
  while rounds < 7:
    # ask user for a guess
    guess = user_guess(allowed_guesses, answers)
    rounds += 1

    # check positions and change display of the guess and the keyboard
    points = check_guess(guess, answer)
  
    # display updated squares and letters
    display_game()

    # win & lose condition
    if points == 5:
      print('The word is correct! You won.')
      break
    elif rounds == 6:
      print('The word is incorrect! You lost. The correct answer is ' + answer)
      break


def read_answers():
  with open('words_answers.txt', 'r') as f:
    answers = f.read().splitlines()
  return answers


def read_guesses():
  with open("words_guesses.txt", 'r') as f:
    guesses = f.read().splitlines()
  return guesses


def user_guess(allowed_guesses, answers):
  while True:
    guess = input('Pick a word: ').upper()
    if len(guess) != 5:
      display_game('Word has to be five letters long.')
    elif not guess.isalpha():
      display_game('Word has to contain only letters.')
    elif not guess.lower() in allowed_guesses and not guess.lower() in answers:
      display_game('Choose a word that exists in a dictionary.')
    else:
      return guess


def check_guess(guess, answer):
  points = 0
  display = [0, 0, 0, 0, 0]
  
  for i in range(0, 5):
    # inizialize all to red
    display[i] = Back.RED + guess[i] + ' ' + Style.RESET_ALL + ' '
    keyboard[guess[i]] = Back.RED
    
    # check if the letter is in correct , change display to green
    if guess[i] == answer[i]:
      display[i] = Back.GREEN + guess[i] + ' ' + Style.RESET_ALL + ' '
      keyboard[guess[i]] = Back.GREEN
      points += 1
      # for proper display of yellow letters in case double-letter word typed:
      answer.replace(answer[i], ' ')
      
  # separate loop for proper display of double-letter words
  for i in range(0, 5):
    # check if the letter is in the answer word, change display to yellow
    if guess[i] != answer[i] and guess[i] in answer:
      display[i] = Back.YELLOW + guess[i] + ' ' + Style.RESET_ALL + ' '
      keyboard[guess[i]] = Back.YELLOW
      
  displays.append(''.join(display))
  return points


def display_game(message=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  # display words
  print('')
  for i in range(0, 6):
    if i < rounds:
      print(displays[i])
      print('')
    else:
      for j in range(0, 5):
        print(Back.WHITE + '  ' + Style.RESET_ALL + ' ', end="")
      print('\n')
  print('')

  # display keyboard, initialize all values to "white"
  if rounds == 0:
    for k in string.ascii_uppercase:
      keyboard[k] = Back.WHITE

  for k, v in keyboard.items():
    print(Fore.BLACK + v + k + ' ' + Style.RESET_ALL + ' ', end="")
    if k == 'M':
      print('\n')
  print('\n' * 2)
  
  if message:
    print(message)
    print('')


if __name__ == "__main__":
  main()
