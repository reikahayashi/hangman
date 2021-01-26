import random
from words import words
import string
#freeCodeCamp

def only_letters(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = only_letters(words)
    word_letters = set(word)  #actual letters
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #letters the user guessed

    tries = 10

   
    while len(word_letters) > 0 and tries > 0:
        
        print(tries, ' tries left. You used these letters: ', ' '.join(used_letters))

        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(' '.join(word_list))

        letter = input("Input a letter ").upper()
        if letter in alphabet - used_letters:
            used_letters.add(letter)
            if letter in word_letters:
                word_letters.remove(letter)
                print('')

            else:
                tries = tries - 1
                print(letter + " is not in the word")

        elif letter in used_letters:
            print("Input a different character")

        else:
            print("Invalid input")
  
    if tries == 0:
        print("You lost. The correct word was " + word)
    else:
        print("You Won!")


hangman()
