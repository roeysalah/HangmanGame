import string
from random import choice
import time

# Global Variables

MAX_GUESSES = 6


def word_select():
    """
    function to select the word to guess from the words.txt file.
    :return: word
    """
    with open("words.txt","r") as file :
        list_of_words = file.readlines()
        choose_word = choice(list_of_words).strip()
    return choose_word


def input_validation(player_input:str,guessed_letters:str)-> bool :
    """
    This function Validates the Player’s Input
    :return: True or False
    """
    return (len(player_input)==1 and player_input in string.ascii_lowercase
            and player_input not in guessed_letters )



def player_input_letter(guessed_letters):
    while True :
        player_input = input("Please Guess a letter:")
        if input_validation(player_input,guessed_letters):
            return player_input



def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))


def building_the_guessed_word (target_word,guessed_letters):
    current_letters = []
    for letter in target_word :
        if letter in guessed_letters:
            current_letters.append(letter)
        else :
            current_letters.append("_")
    return " ".join(current_letters)


def check_game_over(wrong_guess,target_word,guessed_letters):
    return MAX_GUESSES == wrong_guess or set(target_word) <= guessed_letters

def draw_hanged_man(wrong_guesses):
    time.sleep(2)
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])



if __name__ == "__main__":
    while True:
        # Initial setup
        target_word = word_select()
        guessed_letters = set()
        guessed_word = building_the_guessed_word(target_word,guessed_letters)
        wrong_guesses = 0
        print("Welcome to hangman Game:")

        # Game loop

        while not check_game_over(wrong_guesses,target_word,guessed_letters):
            draw_hanged_man(wrong_guesses)
            print("Your Guessed word {}".format(guessed_word))
            print("Current guessed letters: {}\n".
                  format(join_guessed_letters(guessed_letters)))
            player_guess =player_input_letter(guessed_letters)
            if player_guess in target_word:
                print("Great Guess !")
            else :
                wrong_guesses += 1
                if wrong_guesses == 6 :
                    print("Game Over")
                else :
                    print("Incorrect,Please Try Again.")
            guessed_letters.add(player_guess)
            guessed_word = building_the_guessed_word(target_word,guessed_letters)
        draw_hanged_man(wrong_guesses)
        if wrong_guesses == MAX_GUESSES :
            print("You Have Lost The game!")
        else :
            print("You won The Game")
        print("Your Word was {}".format(target_word))

        choose =input("Do You wish To Play Again , please  choose(y/n):")
        if choose == 'n':
            break

    print("Goodbye")

