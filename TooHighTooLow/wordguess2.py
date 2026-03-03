import random

words = ["apple", "banana", "orange", "pear", "grape", "strawberry", "watermelon", "pineapple", "blueberry", "raspberry"]

class wordguess_2:
    def __init__(self):
        # setup self.number to be a random number from 1 to 100
        self.word = random.choice(words)
        # self.guesses to be zero
        self.guesses=0
        pass

    def greeting(self):
        print("Welcome to WordGuess!")

    def start_game(self):
        input("Welcome to WordGuess! Would you like to play a round?").upper()
        if input("Welcome to WordGuess! Would you like to play a round? (y/n) ").upper() == 'Y':
            self.play()
        elif input("Welcome to WordGuess! Would you like to play a round? (y/n) ").upper() == 'N':
            self.quit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            self.start_game()
    
    
    def play(self):
        while True:
            pass
            # Get a letter guess from the user.
            guess = input ("I'm thinking of a word. What do you think it is? Go ahead and guess a letter.")
            self.guesses += 1
            # Check *if* the letter guessed is in the secret word.

            # If correct, print a congratulations message with the number of guesses
            if guess == self.number:
                print("You got it.")
            # Exit the loop
                break
            # Check *if* the guess is less than the secret number
            elif guess < self.number:
            # If so, print "Too low!"
                print("Too low! Try a higher number.")
            # Otherwise (the guess must be too high)
            elif guess > self.number:
            # Print "Too high!"
                print("Too high! Try a lower number.")
            # Check *if* the player has made 10 guesses
            if self.guesses >= 10:
                print(f"You're out of guesses, Friend. :( The number was {self.number}")
                break
            # If so, print a message saying they've run out of guesses and reveal the number
            # Exit the loop


def main():
    game = too_high_too_low()
    game.play()


if __name__ == "__main__":
    main()
