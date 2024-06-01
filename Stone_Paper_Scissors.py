import random

class Stone_Paper_Scissors:

    def Game_name():
        game=("Rock, Paper, Scissors.")
        print(game)
        print('-' * len(game))

    def rules():
        print("\nThe rules are simple:\nRock beats scissors (rock crushes scissors)")
        print("Scissors beats paper (scissors cut paper)\nPaper beats rock (paper covers rock)")

    def main_game():
        e = input("Now please start the game to continue (Y/y for Yes) or (N/n for no): ")
        g = "Yy"
        points = 0
        choices = {1: "rock", 2: "paper", 3: "scissors"}
        print(f"Your current points are : {points}")
        while e.lower() in g:
            
            user = int(input("Enter your choice (1 for rock, 2 for paper, or 3 for scissors): "))
            print(f"Your choice : {choices.get(user)}")
            computer = random.randint(1, 3)
            print(f"Computer's choice : {choices.get(computer)}")
            if user == computer:
                print(f"It's a tie!\nYour current points are : {points}")
            elif(user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
                points += 1
                print(f"You win!\nYour current points are : {points}")
                
            else:
                points -= 1
                print(f"Computer wins!\nYour current points are : {points}")

            e = input("Do you wish to continue again (Y/y for Yes) or (N/n for no): ")
            while e.lower() not in ['y', 'n']:
                print("Oops! wrong input, Type (Y/y for Yes) or (N/n for no)")
                e = input("Do you wish to continue again (Y/y for Yes) or (N/n for no): ")

        else:
            print("Thank you for playing")
            print("Hope you enjoyed!")
            print("Your final score is", points)

if __name__ == "__main__":
    Stone_Paper_Scissors.Game_name()
    Stone_Paper_Scissors.rules()
    Stone_Paper_Scissors.main_game()

