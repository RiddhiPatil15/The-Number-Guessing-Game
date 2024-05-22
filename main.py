# The number guessing game
import random

print("Welcome to the Number Guessing Game.")
def game():   
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10 if difficulty == 'easy' else 5
    print(f"You have {attempts} attempts  to guess the number.")
    while attempts>0:
      guess = int(input("Make a guess: "))
      if guess == num:
        print(f"You got it! The answer was {num}.")
        break
      elif guess> num:
        attempts -= 1
        print("Too high. Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
      else:
        attempts -= 1
        print("Too low. Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
      print("You've run out of guesses, you lose.")

ask = str(input("Do you want to play the game? Type 'y' or 'n': ")) 
if ask == 'y':
  game()
else:
  print("Have a nice day! Goodbye!!")
