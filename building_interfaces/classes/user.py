class User:
    '''A user class to represent the users of our application'''
    
    dob = "01/01/1970"
    password = "password"
    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def create(self):
        # Save the user information to a file
        # Create a file to save the user information
        try:
            userFile = open(self.getUserFileName(), "r")
            # Write the user information to the file
            userFile.write(f"firstName:{self.firstName}\n")
            userFile.write(f"lastName:{self.lastName}\n")
            userFile.write(f"dob:{self.dob}\n")
            userFile.write(f"password:{self.password}\n")
            # Close the file
            userFile.close()
            # Provide feedback
            return True
        except:
            return False
            
        
    def retrieve(self):
        # Loads the user information from a file
        print("The user information has been loaded")
        
    def getUserFileName(self):
        return f"{self.firstName}_{self.lastName}.txt"