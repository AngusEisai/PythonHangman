import time
import numpy as np

play = "y"

while play == "y":

    print("Welcome To Hangman")

    with open("./wordlist.txt") as wordslist:
        words = wordslist.readlines()
    new_words = []

    for word in words:
        fixed_word = word.strip("\n")
        new_words.append(fixed_word)
    game_word = np.random.choice(new_words)
    game_word
    user_word = ["_" for x in game_word]
    user_word
    lives = 5
    your_guesses = []

    things = ["wizard", "psychic", "magician", "technologist", "'associate of Angus'", "God", "Spaceman", "hangman-specialist", "Saddo"]

    while "_" in user_word and lives > 0:
        print(f"You have {lives} lives\n")
        time.sleep(1)
        print(f"You have guessed {your_guesses}")
        print(f"This is your word {''.join(user_word)}.\n")
        time.sleep(1)
        user_guess = input("Please make a guess:\n")
        your_guesses.append(user_guess)
        if user_guess in user_word:
            print("you already guessed that letter")
            time.sleep(2)
        elif user_guess.lower() in game_word:
            print(f"Nice! that letter is in the word - you must be some sort of {np.random.choice(things)}?")
            time.sleep(2)
            locs = [index for index, letter in enumerate(list(game_word)) if user_guess == letter]
            for loc in locs: 
                user_word[loc] = user_guess
        else:
            print("that letter is not in the word! \nYou lost a life!")
            time.sleep(2)
            lives -= 1
            

    if "_" not in user_word:
        print("Nice one, you won!\nYou are so cool.")
    elif lives == 0:
        time.sleep(2)
        print("wtf, that was terrible, Sam, is that you?")
        time.sleep(3)
        print(f"the word was {game_word}")
    else:
        print("something has gone wrong")

    play_again = input("Would you like to play again? type y or n\n").lower()

    if play_again == "y" or play_again == "n": 
        play = play_again
    else:
        "you did not sekect a valid input, Bye-Bye"
        break