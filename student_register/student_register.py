program_options = ('Register', 'Login')
selection = ''

reqiured_fields = {
    "firstName": "First Name",
    "lastName": "Last Name",
    "emailAddress": "Email Address",
    "password": "Password",
}

while (selection not in program_options):
    selection = input("Select a program (Register/Login):")

if selection == 'Register':
    #do registration

    user_info = {}

    for field in reqiured_fields.keys():
        user_info[field] = input(f"Enter your {reqiured_fields[field]}: ")

    user_file = open(f"{user_info['emailAddress']}.txt", "w")

    for prop in user_info.keys():
        user_file.write(f"{prop}:{user_info[prop]}\n")

    user_file.close()
else:
    #do login
    emailAddress = ''
    while emailAddress == '':
        emailAddress = input("Enter the email address you used to register: ")

    user_file = open(f"{emailAddress}.txt", "r")

    user_details = {}
    for prop in user_file:
        kvPair = prop.split(":")
        user_details[kvPair[0]] = kvPair[1].strip("\n")

    print(user_details)
    print("Welcome back,", user_details["firstName"])


