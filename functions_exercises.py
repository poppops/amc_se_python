import my_functions

'''
1. Write a function called add_numbers that takes two parameters, a and b, and returns their sum.
2. Create a function called convert_temperature that takes a temperature in Celsius as a parameter and returns 
   the temperature in Fahrenheit. 
   Use the formula: Fahrenheit = (Celsius * 9/5) + 32.
3. Write a function called find_average that takes three numbers as parameters and returns their average.
4. Create a function called is_even that takes a number as a parameter and returns True if the number is even, 
   and False otherwise.
5. Write a function called calculate_discount that takes two parameters: price and discount_percentage.
   It should return the price after applying the discount.

'''

sum = my_functions.add_numbers(7, 9)
print("The sum of 7 and 9 is: ", sum)

Fahrenheit= my_functions.convert_temp(37)
print('37 degrees celcius in Fahrenheit is', Fahrenheit)


average1=my_functions.find_average(int(input('Please enter a number')),int(input('Please enter a number')),int(input('Please enter a number')))
print('The average of the there numbers is', average1)

# Create a function called is_even that takes a number as a parameter and returns True if the number is even, 
#    and False otherwise.

even = my_functions.is_even(9)
print('9 is an even number; ',even)

# 5. Write a function called calculate_discount that takes two parameters: price and discount_percentage.
#    It should return the price after applying the discount.

mprice = my_functions.calculate_discount(20000,30)
print('Your current price is now', mprice)