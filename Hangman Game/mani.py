print("******Welcome to the Hangman game******")

import random
from stages import stages

my_list = ["banana", "mango", "apple"]

Lives = 6
random_item = random.choice(my_list)
print(random_item)
lenght = len(random_item)
replaced = lenght * "_"
print(replaced)

game_over = False
correct_latter = []
while not game_over:
    guess = input("guess the word: ").lower()
    print(guess)

    display = ""
    for word in random_item:
        if word == guess:
            display += guess
            correct_latter.append(guess)
        elif word in correct_latter:
            display += word
        else:
            display += "_"
    print(display)

    if guess not in random_item:
        Lives -= 1
        if Lives==0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[Lives])