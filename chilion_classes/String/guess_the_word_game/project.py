"""
This game will pick a word and the player have to guess that word in 10 chances.

But if the user didn't get to guess the word then he will lose the game.
and if the player got to guess the word then he/she will get 5 points and 10 more chance to play the game with new word.
"""
import random

DICT_OF_WORDS = {	
                    "he":"a boy",
                    "she":"a girl",
                    "car":"four legs",
                    "mountain":"huge",
                    "aeroplane":"air",
                    "laptop":"powerful",
                    "clash":"fight",
                    "bicycle":"two legs",
                    "truck":"big buddy",
                    "python":"sweet language",
                    "minecraft":"exciting",
                    "java":"horrible",
                    "fire":"painfull yet useful",
                    "wood":"hard yet required",
                }

score = 0
INC_DEC = 5
ending = len(DICT_OF_WORDS) - 1


def get_random_word():
    word = random.choice(list(DICT_OF_WORDS.keys()))
    hint = DICT_OF_WORDS.get(word)
    return word, hint

def main():
    global score
    global INC_DEC
    global ending
    count = 0

    while score >= 0 and count <= ending:
        status = False # it will keep track if the user's last try was successful or not
        # get the random word and its hint
        word, hint = get_random_word()
        print("-----------------------------------------------------------")
        print("HINT -", hint, f"SCORE: {score}".rjust(50))
        print("-----------------------------------------------------------")
        print("\nYou have 10 chances to guess the word")

        # you have write a program to let player guess the word for ten times.
        for i in range(10):
            userIn = input("Word please: ").strip()
            if userIn == word:
                score += INC_DEC #incrementing the score
                status = True
                break
            else:
                print("😌 Wronge selection", end="")
                print(f"chances left- {10-(i+1)}".rjust(50))
        if not status:
            score -= INC_DEC #decrementing the score
        # keep track of how many times we have played the game.
        count += 1

    else:
        if count >= ending:
            print("You have played enough! Start this game again.")
        elif score < 0:
            print("You lost the game 😌😌")

if __name__ == '__main__':
    main()
