from tkinter import *
from tkinter import messagebox
from calculations import *

app = Tk()
app.title("Simple Calculator")

instructions = Label(app, text="Enter 2 numbers and choose an operation.")
instructions.pack(padx=20, pady=5)

inputsFrame = Frame(app)

input1Lbl = Label(app, text="Number 1:")
input1Lbl.pack(side=LEFT, padx=15)

input1Entry = Entry(app)
input1Entry.pack(side=LEFT)

input2Lbl = Label(app, text="Number 2:")
input2Lbl.pack(side=LEFT, padx=15)

input2Entry = Entry(app)
input2Entry.pack(side=LEFT)

inputsFrame.pack(padx=10, pady=30)

def handleAdd():
    # get number1
    number1 = input1Entry.get()
    # get number2
    number2 = input2Entry.get()
    
    # validate the input (make sure they are numeric)
    try:
        validateInput(number1)
        validateInput(number2)
    except:
        messagebox.showerror("Invalid Input", "Input should be numeric only")
        return

    # call the add function
    result = add(number1, number2)
    
    # update the interface with the result
    resultsLbl.configure(text=result)
    
def handleSubtract():
    number1 = input1Entry.get()
    number2 = input2Entry.get()
    
    try:
        validateInput(number1)
        validateInput(number2)
    except:
        messagebox.showerror("Invalid Input", "Input should be numeric only")
        return

    result = subtract(number1, number2)
    resultsLbl.configure(text=result)
    
def handleMultiply():
    return handleOperation("multiply")

def handleDivide():
    return handleOperation("divide")
    
def handleOperation(operation):
    number1 = input1Entry.get()
    number2 = input2Entry.get()
    
    try:
        validateInput(number1)
        validateInput(number2)
    except:
        messagebox.showerror("Invalid Input", "Input should be numeric only")
        return

    match(operation):
        case "add":
            result = add(number1, number2)
        case "subtract":
            result = subtract(number1, number2)
        case "multiply":
            result = multiply(number1, number2)
        case "divide":
            result = divide(number1, number2)

    resultsLbl.configure(text=result)
    
    
def validateInput(value):
    if len(value) == 0:
        raise Exception("Input is empty")
    
    float(value)

        
actionsFrame = Frame(app)

addBtn = Button(actionsFrame, text="+", command=handleAdd)
addBtn.pack(side=LEFT, padx=10)

subtractBtn = Button(actionsFrame, text="-", command=handleSubtract)
subtractBtn.pack(side=LEFT, padx=10)

multiplyBtn = Button(actionsFrame, text="x", command=handleMultiply)
multiplyBtn.pack(side=LEFT, padx=10)

actionsFrame.pack(padx=10, pady=10)

resultsLbl = Label(app, text="")
resultsLbl.pack(padx=10, pady=10)

app.mainloop()
