from tkinter import *
# import interface_functions - alternative import syntax
from interface_functions import convertToFarenheit

# Create a window to house our application and set a title
mainWindow = Tk()
mainWindow.title("Temperature Converter")

# Create a label to instruct users on how to proceed
instructions = Label(mainWindow, text="Enter a temperature in Celsius to convert to Farenheit")
instructions.pack(padx=50, pady=20)

# Create a label to display the result. This will start off being empty
resultMessage = StringVar(value=f"Result will display here")
resultLabel = Label(mainWindow, textvariable=resultMessage)

# Create a frame to house the text input (Entry) and the action button
inputFrame = Frame(mainWindow)
tempInput = Entry(inputFrame)

# Create a function that reads the input the user has provided and converts it to farenheit
def convertTemp():
    temp = tempInput.get()
    farenheit = convertToFarenheit(int(temp))
    resultMessage.set(f"{temp} Celsius is {farenheit} Farenheit")
    
convertBtn = Button(inputFrame, text="Convert", command=convertTemp)

# Add the components to the window
# Note that items appear in the order they are packed and not the order variables are created.
tempInput.pack(side=LEFT, padx=10)
convertBtn.pack(side=RIGHT)
inputFrame.pack(padx=20, pady=20)
resultLabel.pack(pady=20)


mainWindow.mainloop()