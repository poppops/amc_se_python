'''
 1. Create a program that prints all numbers from 1 to 20, but skips any number that is divisible by 4 (use continue)
 2. Write a program that asks the user for a series of words and prints each word. 
    The program should stop asking for input if the user types "exit"
'''
for num in range(1, 21):
    if num % 4 == 0:
       continue
    print(num)

while True:
    word = input("Enter a word: ")
    if word == "exit":
        break
        print("You entered: ",word)

'''
Write a program that asks the user for 5 numbers. 
If the user enters a number greater than 100, skip that number and continue with the next (use continue). 
After all inputs, print the valid numbers entered.
'''


'''
Create a program that prints numbers from 1 to 30, but stops completely when it encounters a multiple of 7 (use break).
'''



for num in range(1, 31):
    if num % 7 == 0:
        break
    print(num)
        
number = []
for num in range(5):
    num=int(input('Please input a number: '))
    if num >100:
        continue
    
    number.append(num)
print(number)