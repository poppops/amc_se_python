from classes.student import Student
from classes.shopping_list import ShoppingItem
from classes.task import Task

# Challenge 2

myStudent = Student("Alex")

myStudent.add_grade(85)
myStudent.add_grade(90)
myStudent.add_grade(78)

print(myStudent.average_grade())

studentAverage = myStudent.average_grade()

if studentAverage == False:
    print(f"{myStudent.name} is new. They don't have any grades yet.")
else:
    print(f"{myStudent.name} has an average grade of {myStudent.average_grade()}")

# Challenge 3
shopItem = ShoppingItem(price=1200, name="Laptop", quantity=2)
print(f"The price of {shopItem.name} is {shopItem.price}")
print(
    f"The total for {shopItem.quantity} x {shopItem.name} is ${shopItem.total_cost()}"
)

# Challenge 4
task = Task("Finish OOP exercises")
task.mark_done()
print(f"{task.description}: {task.get_status()}")
