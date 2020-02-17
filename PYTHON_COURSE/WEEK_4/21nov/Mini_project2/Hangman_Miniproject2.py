import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
hidden_word = len(word)*['_']
guesses = 10
available_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
guessed_letters = ""
letters_correct = 0

print("\n|}> HEEEY WELCOME TO THE HANGMAN GAME <{|\n")
print("I am thinking of a word that is", len(word), "letters long.")
print("Here are the available letters: " + available_letters)
print("You have " + str(guesses) + " guesses")

while 