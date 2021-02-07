import random
from words import words

def get_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


    tries = 10

    while len(word_letters) > 0 and tries > 0:
        print("You have ", tries, " tries left")
        print(Letters guessed so far: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list)

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                tries = tries - 1
                print("Letter is not in the word")


        elif user_letter in used_letters:
            print("You used that character previously!")
        else:
            print("That character is Invalid.")

    if tries == 0:
        print("You lost the game. The correct word is ", word)
    else:
        print("You guessed the word", word)


hangman()




