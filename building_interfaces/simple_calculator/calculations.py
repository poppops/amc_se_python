def add(number1, number2):
    return float(number1) + float(number2)

def subtract(number1, number2):
    return float(number1) - float(number2)

def multiply(number1, number2):
    return float(number1) * float(number2)

def divide(number1, number2):
    if float(number2) == 0:
        return False
    else:
        return float(number1) / float(number2)
    
