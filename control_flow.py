# if condition

number = 4

if number == 4:
    print("Number = 4")

if number > 3:
    print("Number is greater than 3")

if number > 3 and number < 5:
    print("Number is 4")

# if-else condition

if number%2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

'''
 ask a user for a number

 If the number is greater than 10 tell the user it is greater than 10

 If the number is less than or equal to 10, tell the user it is less than or equal to 10

 if the number is a multiple of 3 tell the user it is a multiple of 3

 if it is not a multiple of 3 tell the user it is not a multiple of 3

 '''

some_number = int(input("Enter a number: "))

if some_number > 10:
    print("Your number is greater than 10")
else:
    print("Your number is less than or equal to 10")

if some_number%3 == 0:
    print("Your number is a multiple of 3")
else:
    print("Your number is not a multiple of 3")

# if elif else checks multiple conditions

# NOTE: An if-elif-else block will execute the first condition that evaluates as true

if some_number % 2 == 0:
    print(f"{some_number} is an even number")
elif some_number % 3 == 0:
    print(f"{some_number} is a multiple of 3")
else:
    print(f"{some_number} is neither an even number or a multiple of 3")

# loops

fruits = ['apples', 'bananas', 'cherries', 'dates']

for fruit in fruits:
    print(fruit)

for number in range(5):
    print(number)

for number in range(len(fruits)):
    print(f"{number + 1}. {fruits[number]}")

# default: range(number_of_items)
# starting position: range(starting_position, number_of_items)

for number in range(2 ,7):
    print(number)
# increment: range(number_of_items, starting_position, increment)

# Ask a user for a number and output the timestable of that number from 1 to 12

'''
1 x {number} = {answer}
2 x {number} = {answer}
'''
user_number = int(input('Enter a number: '))
for num in range(1,13):
    print(f'{user_number} x {num} = ',user_number*num)