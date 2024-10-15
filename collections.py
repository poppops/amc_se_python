# A set holds unique values. It is mutable
# This means it can be changed after creation
mySubjects = set()

# A tuple cannot be changed once it has been created
# It is non-mutable
manadatory_subjects = ('English', 'French', 'Maths')

mySubjects.update(manadatory_subjects)

# A list holds ordered objects. It is mutable
elective_subjects = [
    "Geography",
    "Economics",
    "Biology",
    "Physics",
    "Additional Maths",
    "ICT",
    "Literature",
    "History",
    "Religious Studies"
]

subjects_offered = int(input("How many subject would you like to add? "))

subjects_chosen = 0

while subjects_chosen < subjects_offered:

    # To choose a subject, enter the corresponding number:
    # [1] Geography, [2] Economics,..., [9] Religious Studies
    print("To choose a subject, enter the corresponding number...")

    # Loop through the list and output all but the last item with a comma and empty space at the end
    i=0
    while i < len(elective_subjects) - 1:
        print(f'[{i+1}] {elective_subjects[i]},', end=' ')
        i+=1

    # For the last item of the list, don't add a comma and end the line with a \n character
    print(f'[{i+1}] {elective_subjects[i]}')

    # Ask the user to select the subject they would like to take
    choice = input(f"Enter subject number (1-{len(elective_subjects)}): ")

    # Add the corresponding subject to the mySubjects set correcting for the index offset
    mySubjects.add(elective_subjects[int(choice)-1])

    subjects_chosen+=1

# Output the list of subjects the user has selected
print(mySubjects)