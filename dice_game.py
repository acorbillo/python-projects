from random import randint

def roll_the_dice():
    return randint(1, 6)
# pwede ma shorten yung function na to
# by using anonymous function instead
# roll_the_dice = lambda: randint(1, 6)
# ganun din sya gamitin: roll_the_dice()

print("Welcome to roll the dice game!!!")
print("Roll the same number twice and you'll win!")

while True:
    first_roll = input("\nEnter \"r\" to roll the dice\n>>> ")
    if first_roll.lower() == "r":
        print("Rolling the dice...")
        dice_1 = roll_the_dice()
        print(f"Your first roll is: {dice_1}")
        
        while True:
            sec_roll = input("Enter \"r\" again for the second roll\n>>> ")
        
            if sec_roll.lower() == "r":
                break
            else:
                print("Invalid input")
                
        print("Rolling the dice...")
        dice_2 = roll_the_dice()
        print(f"Your second roll is: {dice_2}")
        
        if dice_1 == dice_2:
            print("You won!")
        else:
            print("You lost.")
        
        cont = input("\n\nDo you want to play again?\nEnter \"y\" if yes or any key for no\n>>> ")
        if cont.lower() == "y":
             continue
        else:
             print("Goodbye!")
             break
        
    else:
        print("Invalid input")
