'''

Create a program that writes user information to a text file in the format;

key:value

Capture the following information from a user: first name, last name, email address, password
and save the information to a file {emailaddress}.txt - for example, if the user provides the email
address user@email.com the associated text file should be user@email.com.txt


Part 2.

Amend the program to start by asking the user what action they would like to complete.

Option 1: Save information to user file
Option 2: Retrieve information from a user file

If the user chooses option 1, execute the block of code we have just created in part 1.

If the user chooses option 2, ask for their email address and retrieve their information from their file.


'''

reqiured_fields = {
    "firstName": "First Name",
    "lastName": "Last Name",
    "emailAddress": "Email Address",
    "password": "Password",
}

user_info = {}

for field in reqiured_fields.keys():
    user_info[field] = input(f"Enter your {reqiured_fields[field]}: ")

user_file = open(f"{user_info['emailAddress']}.txt", "w")

for prop in user_info.keys():
    user_file.write(f"{prop}:{user_info[prop]}\n")

user_file.close()

