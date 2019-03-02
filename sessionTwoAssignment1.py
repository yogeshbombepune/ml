import random

print("What is your name?")
name = input()
print("Well {0}, I'm thinking of your number between 1 to 20. ".format(name))
randomNumber = random.randint(1, 20)
print("Take a guess")
while True:
    userNumber = int(input())
    if userNumber == randomNumber:
        print("You guess it.")
        break
    elif userNumber > randomNumber:
        print("Your guess is too high")
    else:
        print("Your guess is too low.")


