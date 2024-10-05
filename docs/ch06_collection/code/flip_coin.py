import random

SIDES = ("Head", "Tail")

def flip_coin():

    # Simulate a coin flip (0 for Heads, 1 for Tails)
    return random.choice(SIDES)

def coin_flip_game():
print("Welcome to the Coin Flip Game!")

    # Ask the user to guess the result of the coin flip
    guess = input("Guess the coin flip result (Head/Tail): ").capitalize()

    # Flip the coin
    result = flip_coin()

    # Compare the guess with the actual result
    if guess == result:
        print(f"Congratulations! It's {result}, you guessed it right.")
    else:
        print(f"Sorry! It's {result}. Better luck next time.")

# Run the game

if **name** == "**main**":
coin_flip_game()
