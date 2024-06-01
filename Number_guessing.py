import random

def NumberGuessing():
    total_rounds = 0
    total_attempts = 0
    max_attempt = 10

    while True:
        total_rounds +=1
        computer_choice= random.randint(1,100)
        no_of_attempts=0
        has_guessed_correctly=False
        
        print("#Instruction")
        print(f"You get a total of {max_attempt} attempts and enter choice between 1 to 100 only")

        
        while(no_of_attempts < max_attempt):
            no_of_attempts+=1
            print(f"Attempt {no_of_attempts} :")
            user_choice= int(input("Enter you choice between 1 to 100 : "))
            
            if(user_choice==computer_choice):
                print("Congrats! you won\nYou have gueesed the correct number\n")
                has_guessed_correctly=True
                break;
            elif(user_choice>computer_choice):
                print("Your choice is too high")
                
            elif(user_choice<computer_choice):
                print("Your choice is too low")
                
            else:
                print("Error! invalid input")
                
        total_attempts += no_of_attempts
        
        if not has_guessed_correctly:
            print(f"Bad Luck! You've used all your attempts. The correct answer was {computer_choice}.")
        
        response= input("Do you want to play another round? (yes/no): ")
        play_again= response.lower() == "yes"
        
        if not play_again:
            break
    
    print(f"\nGame over. You played {total_rounds} round with a totat of {total_attempts} attempts.")

NumberGuessing()
