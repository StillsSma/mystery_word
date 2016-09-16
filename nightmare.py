import random

def menu():
    play_again = input("Play again? y/n?: ")
    if play_again == "y":
        mystery_word_game()
    else:
         exit()


def mystery_word_game():
    open_file = open("/usr/share/dict/words")
    contents = open_file.read()
    contents = (contents.replace("\n", " "))
    contents = contents.lower()
    contents = contents.split(" ")
    open_file.close()
    print ("Welcome to the Hangman game!")

    player_difficulty = input("Please select your difficulty: \n easy medium hard: ")
    player_difficulty = player_difficulty.lower()
    if player_difficulty == "easy":
        while True:
            num = [4,5,6]
            computer_word = (random.choice(contents))
            if len(computer_word) not in num:
                continue
            else:
                break
    elif player_difficulty == "medium":
        while True:
            num = [6,7,8,9,10]
            computer_word = (random.choice(contents))
            if len(computer_word) not in num:
                continue
            else:
                break
    elif player_difficulty == "hard":
        while True:
            computer_word = (random.choice(contents))
            if len(computer_word) > 10:
                break
    else:
        print ("{} is not a difficulty setting".format(player_difficulty))
        mystery_word_game()
    print ("The computer's word contains {} letters".format(len(computer_word)))
    print (computer_word)
    blankspace = "_ " * len(computer_word)
    blankspace = blankspace.split(" ")
    print (*blankspace)
    computer_word = list(computer_word)
    playerguesses = []
    turn = 1
    shuffle = 0
    while turn <= 8:
        answer = []
        print ("turn {}".format(turn))
        print (computer_word)
        playerguess = (input("Please guess a letter: "))
        playerguess = playerguess.lower()
        print (computer_word)
        if len(playerguess) > 1:
            print ("Only one character please!")
        # elif playerguess in playerguesses:
        #    print ("You've already guessed that, try again")
        elif playerguess in computer_word:
            contents = [word for word in contents if len(word) == len(computer_word)]
            playerguesses.append(playerguess)
            for current_location, current_letter in enumerate(computer_word):
                if current_letter == playerguess:
                    answer.append(current_location)
            for item in answer:
                blankspace[int(item)] = computer_word[int(item)]
                contents = [word for word in contents if word[int(item)] == computer_word[int(item)]]
            print (*blankspace)
            print (contents)
            if shuffle == 0:
                print("Woah man, you got one.  At this rate your sure to win *snicker*")
            elif shuffle == 1:
                print("Huh, you got another one.  No, that's cool, gimme a sec")
            elif shuffle == 2:
                print("Hnnnnnggg nope that's, fine, totally fine.")
            elif shuffle == 3:
                print("Uh, uh, uh, uh ,uh")
            else:
                print ("FFFFFFFFFFFFFFFFF")
            computer_word = (random.choice(contents))
            shuffle +=1
            if "_" not in blankspace:
                print ("Thhhhhhat's impossible!!!!")
                break
        else:
            playerguesses.append(playerguess)
            print ("Ha, not even close, give it up.")
            print (*blankspace)
            turn += 1
    computer_word = ''.join(computer_word)
    print ("my word was...")
    print (computer_word)
    menu()


mystery_word_game()
