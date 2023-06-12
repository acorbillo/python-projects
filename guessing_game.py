name = input("what's your name?: ")
print("hello " + name + ", welcome to my guessing game! ")

def guessing_game():

    secret_word = "apple"
    guess = ""
    hint = "the word is composed of 5 letters, a fruit, starts with a letter A"
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False


    while guess != secret_word and not(out_of_guesses):
        if guess_count < guess_limit:
            print(hint)
            guess = input("please enter a guess: ")
            guess_count += 1
            if guess_count < guess_limit and guess != secret_word:
                print("nope that's not it")
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("you are out of guesses. you lose!")
    else:
        print("you win! thank you for playing :)")
        exit()

    restart = input("want to try again?: ")
    if restart == "yes":
        guessing_game()
    else:
        print("thank you for playing!")
        exit()

guessing_game()
