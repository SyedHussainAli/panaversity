import random


def guess_the_number():
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    guess = int(input("Enter your guess: "))
    while guess != number:
        if guess < number:
            print("Higher!")
        else:
            print("Lower!")
        guess = int(input("Enter your guess: "))
    print("Congratulations! You guessed the number.")   
    
if __name__ == "__main__":
    guess_the_number()