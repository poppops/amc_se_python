# Create an empty shopping list
shoppingList = []

# Create a flag to control our while loop
flag = True

while flag:
    listItem = input(
        "What would you like to add to the shopping list? (When finished send an empty item)")

    # If the user sends an empty item, assume the list is complete
    if (len(listItem) == 0):
        flag = False
    else:
        #otherwise add the item to the shopping list
        shoppingList.append(listItem)
        print("Here's your list so far:", shoppingList)

# When the list is complete, display the users shopping list
print("Here's your shopping list: ", shoppingList)

# Write a loop that asks the user what quantity of each item in the shopping list they want to buy

shoppingQuantities = []

index = 0
while index < len(shoppingList):
    shoppingQuantities.append(input(f"What quantity of {shoppingList[index]} do you want?"))
    index += 1

print(shoppingList)
print(shoppingQuantities)
# Store the quantities in a new list called shoppingQuantities

# We need {quanity} of {item}



