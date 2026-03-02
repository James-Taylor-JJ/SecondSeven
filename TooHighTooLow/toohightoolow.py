# a simple high low number guessing game.
#
class too_high_too_low:
    def __init__(self):
        # setup self.number to be a random number from 1 to 100
        # self.guesses to be zero
        self.guesses=0
        pass

    def play(self):
        while True:
            pass
            # Get a number guess from the user (between 1 and 100)
            guess = int(input ("I'm thinking of number between 1 and 100. What do you think it is?"))
            # Convert the input to an integer
            # Increment the number of guesses by 1
            self.guesses += 1
            # Check *if* the guess equals the secret number
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
