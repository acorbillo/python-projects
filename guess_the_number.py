import random

print("Hello! Welcome to guess the number game :)")
name = input("What's your name? ")
print("Hello", name, "! Let's start!")

def guess_the_number():
    n = random.randint(1, 10)
    guess = ""
    guess_count = 0
    guess_limit = 3
    game_over = False

    while n != "guess" and not(game_over):

        if guess_count < guess_limit:
            print("number of guess/es left: ", guess_limit - guess_count)
            try:
                guess = int(input("Guess an integer from 1 to 10: "))
                guess_count += 1
                if guess < n:
                    print ("guess is low")
                elif guess > n:
                    print ("guess is high")
                else:
                    print ("you guessed it!")
                    restart = input("Do you want to play again? Y/N ")
                    if restart == "y" or restart == "Y":
                        guess_the_number()
                    elif restart == "n" or restart == "N":
                        print("thank you for playing! ")
                        exit()

            except ValueError:
                print("invalid input")

        else:
            game_over = True
            print("sorry you lose! ")
            restart = input("Do you want to play again? Y/N ")
            if restart == "y" or restart == "Y":
                guess_the_number()
            elif restart == "n" or restart == "N":
                print("thank you for playing!")
                exit()

guess_the_number()
