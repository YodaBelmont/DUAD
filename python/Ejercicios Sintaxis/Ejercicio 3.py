import random

number = random.randint(1, 10)
x = 11
while (x != number):
    x = int(input("Please enter a number from 1 to 10: "))

print("You Guessed")