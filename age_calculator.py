'''
 Create a program called age_calculator.

 The age calculator should receive the year of birth of a user.
 It should use this to calculate how old the user will be by the end of the current year.
 Output the value to the user in the format:

 "By the end of 2024 you will be {age} years old."
'''

currentYear = 2024
yearOfBirth = input("What year were you born in? ")

# Check that the year is provided as a number
if (yearOfBirth.isdigit() == False):
    yearOfBirth = input("What year were you born in? Please provide the value as a number")

# Check that the year provided is not greater than 2024
if (int(yearOfBirth) > currentYear):
    yearOfBirth = input("You cannot be born in the future. Please enter a year in or before 2024 ")

age = currentYear - int(yearOfBirth)

print(f"By the end of 2024 you will be {age} years old")
