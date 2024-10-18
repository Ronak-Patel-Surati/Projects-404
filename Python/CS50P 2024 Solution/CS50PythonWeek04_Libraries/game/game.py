##checklist
# take +ve int
# random between 1 -n
# Too Small
# Too large
# Just right
import random

# inpit
while True:
    try:
        inte = input("Level: ")
        if inte.isnumeric():
            inte = int(inte)
        else:
            raise Exception
        if inte > 0:
            break
        else:
            raise Exception
    except:
        pass

# initialised the random
n = random.randint(1, inte)
guess = 0

while guess != n:
    guess = input("Guess: ")
    if guess.isnumeric():
        guess = int(guess)
    else:
        continue
    if guess > n:
        print("Too large!")
    elif guess < n:
        print("Too small")
    else:
        print("Just right!")
