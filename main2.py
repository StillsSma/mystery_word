import random
open_file = open("/usr/share/dict/words")
contents = open_file.read()
contents = (contents.replace("\n", " "))
contents = contents.split(" ")

computer_word = (random.choice(contents))
open_file.close()

# Second way to open a file
