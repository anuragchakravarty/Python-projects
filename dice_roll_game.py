#Project :-
'''
Design a project where as an input student will give a static number (between 1 to 6) and then
roll the dice which randomly generate some value between 1 to 6. The winning situation arrives
when the given static/fixed number exactly same to the number came after rolling the dice.
User can play the game as many numbers of times he wants until user wants to exit, and
whenever winning situation occur some scores must be given to the user, and these scores
goes on adding if user play this game multiple number of times.
Note: Dice contains face value’s (1 to 6)
'''

import random

def rules():
    print("Rules of the game:-")
    print("You have to choose a number from 1 to 6, if your input and input of the diceroll is same then you will be rewarded by (+10 points)")
    print("If your input and input of the diceroll is not same then you loose")
    print("The game will be starting with 0 points")
    print("This will continue untill you stop the game or type any wrong input\n")

def game():
    e = input("Now please start the game to continue (Y/y for Yes) or (N/n for no): ")
    g = "Yy"
    points = 0
    attempts = 0
    l1 = ["Y", "y", "N", "n"]

    while e in g:
        print(f"Your current points are {points}")
        print("Enter your number of choice between 1 to 6")
        a = int(input("Enter your choice: "))
        c = random.randint(1, 6)

        if a == c:
            points += 10
            attempts += 1
            print(f"The diceroll gave the number {c}")
            print("You won")
            print(f"Your current points are: {points}\n")
        elif a > 6 or a < 1:
            print("Invalid input, Enter number between 1 to 6!")
        else:
            points = points
            attempts += 1
            print(f"The diceroll gave the number {c}")
            print("Since the dice rolled number and your choice are not the same")
            print("You lost")
            print(f"Your current points are: {points}\n")

        e = input("Do you wish to continue again (Y/y for Yes) or (N/n for no): ")
        while e not in l1:
            print("Oops! wrong input, Type (Y/y for Yes) or (N/n for no)")
            e = input("Do you wish to continue again (Y/y for Yes) or (N/n for no): ")

    else:
        print("\nThank you for playing")
        print("Hope you enjoyed!")
        print(f"Your final score is {points} and total no. of attempts are {attempts}")

rules()
game()
