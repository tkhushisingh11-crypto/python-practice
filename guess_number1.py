import random

number = random.randint(1, 100)

print("Guess the number game!")
print("I hava choosen a number between 1 and 100.")
print("You hava 7 attempts.")

for attempt in range(1, 8):
    guess = int(input(f"Attempt {attempt}/7 - Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number!")
        break

else:
    print("You used all 7 attempts.")
    print("The number was: ",number)
