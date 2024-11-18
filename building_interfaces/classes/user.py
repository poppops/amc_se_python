import os


class User:
    """A user class to represent the users of our application"""

    dob = "01/01/1970"
    password = "password"

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def create(self):
        # Save the user information to a file
        # Create a file to save the user information
        try:
            userFile = open(self.getUserFileName(), "w")
            # Write the user information to the file
            # Implement writing to file using a loop with the dir() function
            for attr in dir(self):
                if attr[0] != "_" and attr not in (
                    "create",
                    "retrieve",
                    "getUserFileName",
                ):
                    userFile.write(f"{attr}:{getattr(self, attr)}\n")

            # Close the file
            userFile.close()
            # Provide feedback
            return True
        except:
            return False

    def retrieve(self, password):
        # Loads the user information from a file
        if not os.path.exists(self.getUserFileName()):
            return False

        with open(self.getUserFileName(), "r") as file:
            for line in file:
                key, value = line.split(":")
                setattr(self, key, value.strip())

        if password.strip() == self.password:
            return True
        else:
            print("Passwords didn't match", f"{password}:{self.password}")
            return False

    def getUserFileName(self):
        return f"{self.firstName}_{self.lastName}.txt"
