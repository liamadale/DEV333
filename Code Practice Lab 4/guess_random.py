def ask_name():
    name = input("What is your name? ")
    print(f"Hello, {name}!")
    return name

def ask_difficulty():
    difficulty = input("Choose a difficulty level (EASY, MODERATE, HARD): ").strip().upper()
    if difficulty == "EASY":
        return 5, 10
    elif difficulty == "MODERATE":
        return 8, 100
    elif difficulty == "HARD":
        return 10, 1000
    else:
        print("Invalid choice. Please choose again.")
        return ask_difficulty()
    

def guess_number(difficulty, session):
    import random
    limit = difficulty[0]
    upper_limit = difficulty[1]
    number_to_guess = random.randint(1, upper_limit)
    guess = None

    while guess != number_to_guess and limit > 0:
        try:
            guess = int(input(f"Guess a number between 1 and {upper_limit}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if guess < number_to_guess:
            print("Too low! Try again.")
            limit -= 1
        elif guess > number_to_guess:
            print("Too high! Try again.")
            limit -= 1
        else:
            print("Congratulations! You've guessed the right number.")
            session["win"] += 1
            break
    if limit == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        session["loss"] += 1

print("Welcome to the Guessing Game!")
name = ask_name()
session = {"win": 0, "loss": 0}
while True:
    difficulty = ask_difficulty()
    guess_number(difficulty, session)
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print(f"Thanks for playing, {name}!")
        print(f"Total Wins: {session['win']}, Total Losses: {session['loss']}")
        break
    else:
        print("Starting a new game...")
