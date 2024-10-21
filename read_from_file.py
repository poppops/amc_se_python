my_poem = open("my_poem.txt", "r")

for line in my_poem:
    print(line, end="")

my_poem.close()