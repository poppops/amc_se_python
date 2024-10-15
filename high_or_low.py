import random

# Generate 2 random numbers between 1 and 9
number1, number2 = random.randint(1,9), random.randint(1,9)

# Check that the two numbers are not identical and if they are generate a new set
while number1 == number2:
    number1, number2 = random.randint(1, 9), random.randint(1, 9)

# Reveal the first number to the user and ask them to guess if the next number will be higher or lower
print(f"The first number is {
      number1}. Guess if the next number is higher or lower!")

# The  user should enter > if they think the number will be higher or < if they think it will be lower
guess = input(
    "Enter '>' if you think the second number is higher or '<' if you think it is lower: ")

# Compare their guess to the actual result and let them know if they are right or wrong
while guess != ">" and guess != "<":
    guess = input(
        "Enter '>' if you think the second number is higher or '<' if you think it is lower: ")

if guess == ">":
    if number2 > number1:
        print(f"You're right! The second number is {number2}")
    else:
        print(f"Wrong, the second number is {number2}")
elif guess == "<":
    if number2 < number1:
        print(f"You're right! The second number is {number2}")
    else:
        print(f"You're wrong! The second number is {number2}")
