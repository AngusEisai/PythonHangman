import time
import numpy as np
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
""")

dead = '''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  |
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y|
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | |
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : : 
. .          `'       . .
'''
play = "y"
numbers = [0.1, 0.2, 0.3]
text = "Welcome To Hangman!\n"
for l in text:
    print(l, end="")
    time.sleep(np.random.choice(numbers))
time.sleep(3)
player = input("Who is playing? please type your name:\n")

checks = "sam samuel samwise sammy westbrook sammich, Psalm, salmon".split(" ")

if player.lower() in checks:
    time.sleep(1)
    text = f"Sorry {player}. I am instructed not to play with you.\n\n Please leave.\n\n"
    for l in text:
        print(l, end="")
        time.sleep(np.random.choice(numbers))
else:
    time.sleep(1)
    print(f"Nice to meet you {player}, lets play!")

    while play == "y":

        
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

        things = ["you must be some sort of wizard", "are you psychic", "I bet you are a magician", "I can see why you are a technologist", "this is what I expected of an associate of Angus", "you are genuinely greater than a God", "you could be a Spacewoman!", "Woah! am I playing with a hangman-specialist?", "thats actually kinda sad"]

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
                print(f"Nice! '{user_guess}' is in the word - {np.random.choice(things)}")
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
            print(dead)
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
            "you did not select a valid input, Bye-Bye"
            break