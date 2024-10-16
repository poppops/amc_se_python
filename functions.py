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
