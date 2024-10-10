amountToPay = input("How much does the customer owe? ")
amountReceived = input("How much has the customer paid? ")

print("amountToPay is ", type(amountToPay))
print("amountReceived is", type(amountReceived))
print("amountToPay is now ", type(int(amountToPay)))
print("amountReceived is now", type(int(amountReceived)))

changeDue = int(amountReceived) - int(amountToPay)

print(f"Return {changeDue} to the customer")
