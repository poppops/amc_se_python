# # Defining a simple function

# '''
# To define a function we use the `def` keyword, followed by the function name and brackets then end
# with a colon

# def functionName():
#     indendented code is executed as part of the function
#     indendented code is executed as part of the function
# '''

# def myFunction():
#     print("This is my first function")

# '''
# To execute a function, we type the function name followed by brackets
# '''

# myFunction()

# '''
# We can execute the same block of code by calling the function multiple times
# '''

# myFunction()
# myFunction()
# myFunction()

# # Create a function called intro which outputs "Hello, my name is My Name"

# def intro():
#     print("Hello, my name is My Name")

# # Varibales defined outside of any function are called Global variables
# # They can be accessed from anywhere in the program
# name = input("What's your name? ")

# def greeting():
#     print(f"Hello {name}, it's nice to meet you")

# greeting()


# # Variables defined inside a function are called local variables
# # They only exist inside the function in which they were defined

# yearOfBirth = int(input("What year were you born in? "))

# def greeting2():
#     age = 2024 - yearOfBirth
#     print(f"Hello {name}, you look like you're {age} years old")

# greeting2()

# # The varibale 'age' does not exist outside of the greeting2 function
# #print(age)

# # def whatTimeIsIt():
# #     print(f"The time is currently: {currentTime}")

# # whatTimeIsIt()
# # currentTime = "7:15"

# # Using arguments means we don't have rely on globally defined variables for our functions to work

# def greeting3(name):
#     print(f"Hello {name}, it's nice to meet you!")

# greeting3("Suhmayah")
# greeting3("Ryan")
# greeting3("Blessing")
# greeting3("Fotsing")
# greeting3("Akika")

# greeting3(input("What's your name?"))

# Create a function that receives a name and favourite colour as arguments and outputs:
# Hi, my name is {name} and my favourite colour is {colour}
def greeting4(name,colour):
    print(f"Hi,my name is {name} and my favourite colour is {colour}")


#greeting4(input("Please enter your name: "),input("Please enter your favourite colour: "))

myName = "Tancho"
myFavouriteColour = "red"

greeting4(myName, myFavouriteColour)

'''
1. Create a function called calculate_area that takes two arguments, length and width, and 
 prints the area of a rectangle.
'''

def calculate_area(length, width):
    area = length * width
    print(f"The area of the rectangle is {area}")

calculate_area(7,4)


'''
2. Write a function called find_max that takes three numbers as arguments and prints the largest of the three.
'''
def find_max(num1, num2, num3):
    # numbers = [num1, num2, num3]
    # largest_number = max(numbers)
    largest_number = max(num1, num2,num3)
    print("The largest number is", largest_number)

find_max(28,13,15)


# Find out if a number is a prime number

def is_prime_number():
    is_prime = True
    for num in range(2, random_number):
        if random_number%num == 0:
            print(random_number, "is divisible by", num)
            is_prime = False
            break

    if is_prime == True:
        print(random_number, "is a prime number")
    else:
        print(random_number, "is not a prime number")

random_number = 27
is_prime_number()

random_number = 53
is_prime_number()

random_number = 87
is_prime_number()

def is_prime_number2(random_number):
    is_prime = True
    for num in range(2, random_number):
        if random_number%num == 0:
            print(random_number, "is divisible by", num)
            is_prime = False
            break

    if is_prime == True:
        print(random_number, "is a prime number")
    else:
        print(random_number, "is not a prime number")

is_prime_number2(7)
is_prime_number2(111)
is_prime_number2(257)

#############
#############
#############

# Named parameters

# Create a function called brief_introduction which accepts 3 arguments; name, age, address.
# The function should print the string "Hello, my name is {name}. I am {age} years old and I live in {address}"

def brief_introduction(name, age, address):
    print(f"Hello, my name is {name}. I am {age} years old and I live in {address}")

brief_introduction("Charlie", 11, "Cardiff")
brief_introduction(name="Matthew", age=7, address="Cardiff")
brief_introduction(address="London", name="Tancho", age=13)
brief_introduction(8, "Yaounde","Suhmayah")

# Create a function called friendly_greeting that accepts a name argument and outputs the string:
# "Hello {name}, it's nice to meet you.". Set a default value for the name argument as "friend".

def friendly_greeting(name = 'friend'):
    print(f"Hello {name}, it's nice to meet you.")
          
friendly_greeting()
friendly_greeting("Adrian")

# Returning values from a function

# def is_a_prime_number(number_in_question):
#     is_prime = True
#     for num in range(2, number_in_question):
#         if number_in_question%num == 0:
#             is_prime = False
#             break

#     return is_prime

# is_prime = is_a_prime_number(73)
# print(is_prime)

# if is_prime:
#     print("73 is a prime number, that was a lucky guess!")
# else:
#     print("73 isn't a prime number")

# if is_a_prime_number(8):
#     print("This function is not working correctly")
# else:
#     is_a_prime_number(input("8 is not a prime number. Try another number"))

# Create a function called area_calculator that calculates and returns the area of a right-angled triangle based on the
# length and width provided to it. Calculate the area of the following 5 triangles and determine which is the largest.
'''
1. Length = 12, Width = 6
2. Length = 17, Width = 4
3. Length = 16, Width = 7
4. Length = 7, Width = 62
5. Length = 34, Width = 19
'''
def area_calculator(length, width):
    area= length * width/2
    return area

area1=area_calculator(12,6)
area2=area_calculator(17,4)
area3=area_calculator(16,7)
area4=area_calculator(7,62)
area5=area_calculator(34,19)

print('the area of triangle 1 is ', area1)
print('the area of triangle 2 is ', area2)
print('the area of triangle 3 is ', area3)
print('the area of triangle 4 is ', area4)
print('the area of triangle 5 is ', area5)

largest_area = max(area2,area1,area3,area4,area5)
print('\n The largest area is ',largest_area )

## v2

triangles = [
    {"length": 12, "width": 6},
    {"length": 17, "width": 4},
    {"length": 16, "width": 7},
    {"length": 7, "width": 62},
    {"length": 34, "width": 19},
]

triangle_areas = []

for triangle in triangles:
    triangle_areas.append(area_calculator(length=triangle["length"], width=triangle["width"]))

print('\n The largest area is ',max(triangle_areas))


    

