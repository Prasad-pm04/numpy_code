import random

# 🎲 Let's generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# 🎉 Welcome message
print("🎯 Welcome to the Number Guessing Game!")
print("🤔 I'm thinking of a number between 1 and 100. Can you guess it?")

# Let's start guessing
attempts = 0

while True:
    # 👤 Ask user for their guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # ✅ Check the guess
    if guess < secret_number:
        print("🔻 Too low! Try a higher number.")
    elif guess > secret_number:
        print("🔺 Too high! Try a lower number.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break  # Exit the loop since the user won
