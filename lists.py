shoppingList =  ["flour", "butter", "sugar", "eggs", "baking powder"]
print("Shopping List: ", shoppingList)

miscellaneous = []
print("Empty List: ", miscellaneous)

miscellaneous.append("Football boots")
print("Item added to the list:", miscellaneous)

print("Items in my shopping list: ", len(shoppingList))

print("The first element of my shopping list is", shoppingList[0])

# Item {n} of the shopping list is shoppingList[n]

index = 0

while index < len(shoppingList):
    print(f"Item {index + 1} of the shopping list is {shoppingList[index]}")
    index += 1