import random

number = random.randint(1, 100)
attempts = 0
guessed = False

print("Guess the number between 1 and 100!")

while not guessed:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You took {attempts} attempts.")
        guessed = True
