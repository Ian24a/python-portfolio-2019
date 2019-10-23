# Ian Christensen
# 10/19
# Hangman Game

# Classic hangman. Computer picks random word
# and the player tries to guess it
# one letter at a time. If they can't guess it
# the stick figure gets hanged

# Imports
import random

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

max_wrong = len(HANGMAN) - 1
words = ("OVERUSED", "CLAM", "GUAM", "TAFETTA", "PYTHON")

#initialize variables
word = random.choice(words)#word to bo guessed
so_far = "-" * len(word)#one dash for each letter in word
wrong = 0# number of wrong guesses player has made
used = []# letters already guessed

print(" Welcome to Hangman. Good luck!")

while wrong < max_wrong and so_far != word:
     print(HANGMAN[wrong])
     print("\nYou've used the following letters:\n", used)
     print("\nSO far, the word is:\n", so_far)

     guess = input("\n\nEnter your guess: ")
     guess = guess.upper()

     while guess in used:
          print("You've already guessed that letter", guess)
          guess = input("\n\nEnter your guess: ")
          guess = guess.upper()

     used.append(guess)
     if guess in word:
          print("\nYes!", guess, "is in the word")

          new = ""
          for i in range(len(word)):
               if guess == word[i]:
                    new += guess
               else:
                    new += so_far[i]
          so_far = new
     else:
          print("\nSorry,", guess, "isn't in the word.")
          wrong += 1
if wrong == max_wrong:
     print(HANGMAN[wrong])
     print("\nYou've been hanged!")
else:
     print("\nYou guessed it!")
print("\nThe word was", word)
input("\n\nPress the enter key to exit.")











          



