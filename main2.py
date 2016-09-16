import random
open_file = open("/usr/share/dict/words")
contents = open_file.read()
contents = (contents.replace("\n", " "))
contents = contents.split(" ")

computer_word = (random.choice(contents))
open_file.close()

if shuffle == 0:
    print("Woah man, you got one.  At this rate your sure to win *snicker*")
elif suffle == 1:
    print("Huh, you got another one.  No, that's cool, gimme a sec")
elif suffle == 2:
    print("Hnnnnnggg nope that's, fine, totally fine.")
elif suffle == 3:
    print("Uh, uh, uh, uh ,uh")
else:
    print ("FFFFFFFFFFFFFFFFF")
