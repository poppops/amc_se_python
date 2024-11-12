### **Exercise: Basic Calculator**

**Objective**: Build a simple calculator interface where users can input two numbers and perform basic arithmetic operations: addition, subtraction, multiplication, and division.

#### **Instructions**

1. **Set Up the Main Window**:
   - Use `Tk()` to create the main window and set an appropriate title (e.g., `"Simple Calculator"`).

2. **Create Input Fields**:
   - Add two `Entry` widgets for users to enter numbers. Label each entry so users know where to type the first and second numbers.

3. **Add Buttons for Operations**:
   - Create four buttons for the operations: `"Add"`, `"Subtract"`, `"Multiply"`, and `"Divide"`.
   - Each button should be linked to a function that performs the respective operation and displays the result.

4. **Display the Result**:
   - Add a label or an entry field to show the result of the calculation.

#### **Hints**
- Use the `.get()` method to retrieve numbers from the entry fields and the `.set()` or `.configure()` methods to display the result in the label.
- Remember to handle cases like division by zero to prevent errors.

#### **Expected Skills**
- Working with basic Tkinter widgets: `Label`, `Entry`, `Button`
- Using simple math operations and linking button commands to functions
- Displaying output with labels or entry fields
