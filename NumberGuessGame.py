import random
def gen_ran_num():
    ran_num = random.randint(1, 100)
    return ran_num
def usr_guess():
    print("Guess a number between 1 and 100.")
    ran_num = gen_ran_num()
    num_of_guesses = 0
    while True:
        try:
            usr_num = int(input("enter your guess: "))
        except ValueError:
            print("That's not a number.")
            continue
        num_of_guesses = num_of_guesses+1
        if usr_num == ran_num:
            print(f"you guessed correctly in {num_of_guesses} guesses")
            break
        elif usr_num < ran_num:
            print("The number is higher")
        elif usr_num > ran_num:
            print("The number is lower")
        print("you have guessed " +str(num_of_guesses) + " times")
usr_guess()

