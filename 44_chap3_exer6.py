# MODIFY NUMBER GUESSING GAME

import random
winning_number = random.randint(1, 100)
guess = 1
user_input = int(input("guess a number between 0 and 100 : "))
game_over = False
while not game_over:
    if user_input == winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over = True
    else:
        if user_input < winning_number:
            print("too low")
            guess += 1
            user_input = int(input("guess again: "))
        else:
            print("too high")
            guess += 1
            user_input = int(input("guess again: "))