# '''
# 1. Write a program that prints all even numbers between 1 and 50. - Ryan
# 2. Check if a number is prime (input from the user). If it is prime, print "Prime"; otherwise, print "Not Prime". - Blessing
# 3. Write a program that prints the sum of all numbers from 1 to 100 that are divisible by 3. - Ryan
# 4. Create a program that asks for 5 numbers from the user, then prints the largest number. - Akika
# 5. Write a program that counts how many vowels are in a given string (input from the user). - Sir
# 6. Create a program that prints the Fibonacci sequence up to the 10th term. - Fotsing
# 7. Write a program that reverses the digits of an integer (input from the user). - Akika
# 8. Check if a word (input from the user) is a palindrome (a word that reads the same forwards and backwards). - Sir
# 9. Write a program that calculates the factorial of a number (input from the user). - Blessing
# 10.Create a program that prints all numbers from 1 to 100, but for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", 
#    and for multiples of both 3 and 5 print "FizzBuzz". - Fotsing


# '''
# for even_number in range(1,50):
#     if even_number %2 ==0:
#         print(even_number)

# # number 2
# number=int(input('Please enter a number'))
# is_prime = True
# for run in range(2,number):
#     if (number)% run == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")

# # 3. Write a program that prints the sum of all numbers from 1 to 100 that are divisible by 3. - Ryan
# total=0
# for num in range(1,13):

#     if num%3==0:
#         total+=num
        
# print(total)        

# # 4. Create a program that asks for 5 numbers from the user, then prints the largest number. - Akika

# numbers = []
# for i in range(5):
#     number = int(input(f"Enter a number {i + 1}"))
#     numbers.append(number)

# highest_number = max(numbers)
# print(highest_number)

# # 5. Write a program that counts how many vowels are in a given string (input from the user). - Sir
# sentence = input("Enter a string to find out how many vowels it contains: ")

# vowels = ('a', 'e', 'i', 'o', 'u')
# vowel_count = 0

# for letter in sentence.lower():
#     if letter in vowels:
#         vowel_count += 1

# print(f"There are {vowel_count} vowels in the sentence '{sentence}'")

# # 6. Create a program that prints the Fibonacci sequence up to the 10th term. - Fotsing

# x=y=1
# while y< 100:
#     print(y)
#     x,y = y, x+y

# # 7. Write a program that reverses the digits of an integer (input from the user). - Akika

# random_number = input("Enter any number: ")

# current_character = len(random_number) - 1
# reversed_number = ''
# while (current_character >= 0):
#     reversed_number += random_number[current_character]
#     current_character-= 1

# print(f"{random_number} reversed is {reversed_number}")

# # 8. Check if a word (input from the user) is a palindrome (a word that reads the same forwards and backwards). - Sir

# palindrome = input("Enter a word that reads forward and backward")

# current_character =len(palindrome) - 1
# reversed_string = ""
# while(current_character >= 0):
#     reversed_string += palindrome[current_character]
#     current_character -= 1

# print("Reversed String:",reversed_string)

# if palindrome == reversed_string:
#     print(palindrome, "is a palindrome")
# else:
#     print(palindrome, "is not a palindrome")

# # 9. Write a program that calculates the factorial of a number (input from the user). - Blessing

# factorial=int(input('Please enter a number'))
# i=1
# j=1
# while i<= factorial:
#     j*=i
#     i+=1
# print(j)

# #  10.Create a program that prints all numbers from 1 to 100, but for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", 
# #    and for multiples of both 3 and 5 print "FizzBuzz". - Fotsing
# l=100

# if (l%==3):
#     print('Fizz')
# elif(l%==5):
#     print('Buzz', l% 5 )
# elif(l%=3 and l%=5):
#     print('FizzBuzz', l%3 and l%5)
# else:
#     print(l)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)