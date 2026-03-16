import random

def welcome_message():
  print("Welcome to Bulls and Cows!")

def get_secret_code():
  while True:
    ask_code = input("Type '1' if you would like the computer to generate a secret code or '2' if you want to input it yourself:\n")
    if ask_code == "1":
      seed_val = int(input("Please enter a seed:\n"))
      random.seed(seed_val)
      secret_code = ""
      while len(secret_code) != 4:
        random_val = random.randint(0, 9)
        if str(random_val) not in secret_code:
          secret_code += str(random_val)
      return secret_code
    else:
      while True:
        secret_code = input("Type in the secret code:\n")
        if not secret_code.isdigit() or len(set(secret_code)) != len(secret_code) or len(secret_code) != 4:
          print("There was a problem processing your input. Please type exactly four unique digits.")
        else:
          return secret_code


def get_difficulty():
  while True:
    difficulty = input("Choose a difficulty level:\n"
                        "1. Easy (12 guesses)\n"
                        "2. Medium (8 guesses)\n"
                        "3. Hard (5 guesses)\n")
    if difficulty == "1":
      return 12
    if difficulty == "2":
      return 8
    if difficulty == "3":
      return 5
    print("There was a problem processing your input. Please type 1, 2, or 3.")

def get_guess():
  while True:
    guess = input("Guess the code (type 'give up' if you would like to quit the game):\n")
    if guess == "give up":
      return guess
    if not guess.isdigit() or len(set(guess)) != len(guess) or len(guess) != 4:
      print("There was a problem processing your input. Please type exactly four unique digits.")
    else:
      return guess

def play_game():
  secret_code = get_secret_code()
  num_guesses = get_difficulty()
  diff = num_guesses
  while True:
    guess = get_guess()
    if guess == "give up":
      return (False, diff-num_guesses)
    elif guess == secret_code:
      print("You win!")
      return (True, diff-(num_guesses-1))
    else:
      bulls = 0
      cows = 0
      for i in range(len(guess)):
        if guess[i] == secret_code[i]:
          bulls += 1
        elif guess[i] in secret_code:
          cows += 1
      print(f"Bulls: {bulls}")
      print(f"Cows: {cows}")
      num_guesses -= 1
      print(f"You have {num_guesses} guesses left.")
      if num_guesses == 0:
        print(f"You lose; the correct answer was {secret_code}")
        return (False, diff)

if __name__ == "__main__":
  welcome_message()
  while True:
    play_game()
    again = input("Would you like to play again? (y/n):\n")
    if again != "y":
      break
