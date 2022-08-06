# Hangman Game
# The purpose of this game to guess a word in 6 or less tries
# If you reach 6 tries then the game ends. But if you guess it before that then you win.
#
# Objectives
# Create a template game where a word is picked from a word bank and a user gives a letter and the game checks to see if the letter is in the word given
# For every letter that is in the word, fill in the appropriate space and replace the _ with the letter and increase counter by 1
# For every letter that is incorrect, increase guess counter by 1 and how many guesses were used so far
import random

def pickWord(listOfWords):
  # this variable will hold the word bank of available words to choose from
  listOfWords = listOfWords
  
  # chooses a random word from wordBank
  return random.choice(wordBank)

def generateHangman(word):
  print("Welcome to Hangman game!")
  # keeps track of how many guesses were made
  numGuess = 0
  letterToLines = ""

  for letter in word:
    letterToLines += "_"
  print("Guess the word: " + letterToLines)

  while(numGuess != 6):
    guess = input("Enter a letter: ")
      
    if guess in word:
      letterToLines = letterToLines[:word.find(guess)] + guess + letterToLines[word.find(guess) + 1:]
      numGuess += 1
    else:
      numGuess += 1

    print("Guess the word: " + letterToLines)
    print("# of tries used: " + str(numGuess))

    
  
# MAIN PROGRAM STARTS HERE
wordBank = ["red", "blue", "white", "black"]
generateHangman(pickWord(wordBank))