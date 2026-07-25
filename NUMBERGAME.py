import random

secret_number = random.randint(1, 100)
attempt = 0

print("Welcome to Number Guessing Game!")

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempt += 1

    if guess < secret_number:
        print("Too Low!")

    elif guess > secret_number:
        print("Too High!")

    else:
        print("Congratulations!")
        print("You guessed the number in", attempt, "attempts.")
        break555