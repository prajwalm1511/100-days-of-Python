import random

def play_game(attempts):
    comp = random.randint(1, 100)
    for i in range(attempts, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        
        if guess == comp:
            print(f"Correct guess! The answer was {comp}.\nYou win :)")
            return # This exits the function entirely
        elif guess > comp:
            print("Too high.")
        else:
            print("Too low.")
            
    # If the loop finishes without returning, they lost
    print(f"You've run out of guesses. You lose! The number was {comp}.")

print("Welcome to the number guessing game!!")
print("I'm thinking of a number between 1-100")
difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    play_game(10)
else:
    play_game(5)