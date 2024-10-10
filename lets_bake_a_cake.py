'''
Let's bake a cake.

To bake a cake that serves 4 people, you need the following ingredients;

225g of Flour
225g of Butter
125g of Sugar
4 large eggs
2tsp of Baking Powder

Write a program that asks a user how many people they will be serving cake for
and calculates the quantity of ingredients needed.

Output the ingredients as above.
'''

# Calculate the ingredients reqiured for 1 person

flour_pp = 225/4
butter_pp = 225/4
sugar_pp = 150/4
eggs_pp = 4/4
baking_powder_pp = 2/4


# Write a program to calculate the ingredients required for the number of people indictated by
# the user

numberOfPeople = int(input("How many people will you be baking for? "))

total_flour = numberOfPeople * flour_pp
total_butter = numberOfPeople * butter_pp
total_sugar = numberOfPeople * sugar_pp
total_eggs = numberOfPeople * eggs_pp
total_baking_powder = numberOfPeople * baking_powder_pp


# Output the recipe for that many people

print (f"To bake a cake for {numberOfPeople} people you will need:")
print(f"{total_flour}g of flour")
print(f"{total_butter}g of butter")
print(f"{total_sugar}g of sugar")
print(f"{total_eggs} eggs")
print(f"{total_baking_powder}tsp of baking powder")

