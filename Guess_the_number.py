#Easy project python 2(Practice)
import random
def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f'Guess a number betwenn 1 and {x} : '))
        if guess < random_number:
            print("The number is too low")
        elif guess >random_number:
            print("The number is too high")
    print(f"You are right the number was {random_number}")
guess(10)