# myFile = open("output/my_first_file.txt", 'w')
# myFile.write("Hello, world!")
# myFile.close()

# Create a file called user_info.txt
# Receive a message from a user and save it to the file

# user_info = open("output/user_info.txt", "w")
# user_info.write(input("Enter your address: "))
# user_info.close()

poem = "Roses are red,\n"
poem+= "Violets are blue,\n"
poem+= "Sugar is sweet,\n"
poem+= "...\n"

my_poem = open("output/my_poem.txt", "w")
my_poem.write(poem)
my_poem.close

my_poem = open("output/my_poem.txt", "a")
my_poem.write("Author Unknown 2\n")
my_poem.close

edit_my_poem = open("output/my_poem.txt", "r+")

# We can use the read method to read the entire content or a portion of it.
# print("Read(): ", edit_my_poem.read(10))
# print("Read(): ", edit_my_poem.read(10))
# edit_my_poem.seek(0)
# print("Read(): ", edit_my_poem.read(20))
# edit_my_poem.seek(25)
# edit_my_poem.write("Let's add some random text")

# Method 1 - Using seek()
# edit_my_poem.seek(51)
# edit_my_poem.write("And so are you.\n")


# Or we can use a loop to read through the file line by line
line_counter = 1
for line in edit_my_poem:
    print(line)
    if (line_counter == 1):
        edit_my_poem.write("And so are you 1.\n")
        break

    line_counter+=1
    
edit_my_poem.close()
