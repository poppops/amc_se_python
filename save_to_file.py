myFile = open("my_first_file.txt", 'w')
myFile.write("Hello, world!")
myFile.close()

# Create a file called user_info.txt
# Receive a message from a user and save it to the file

user_info = open("user_info.txt", "w")
user_info.write(input("Enter your address: "))
user_info.close()

poem = "Roses are red,\n"
poem+= "Violets are blue,\n"
poem+= "Sugar is sweet,\n"
poem+= "..."

my_poem = open("my_poem.txt", "w")
my_poem.write(poem)
my_poem.close

my_poem = open("my_poem.txt", "a")
my_poem.write("Author Unknown\n")
my_poem.close