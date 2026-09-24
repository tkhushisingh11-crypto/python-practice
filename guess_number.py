import random

number = random.randint(1, 100)

print("Guess the number game!")
print("I have chosen a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number!")
        break