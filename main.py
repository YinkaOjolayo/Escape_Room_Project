import random
small_key = False

def room_1 (a):
    keycard = False
    private_key = False
    escape_1 = False
    global small_key
    while escape_1 == False:
        if a.upper() == "SKELETON" or a.upper() == "SKELE":
            print("You inspected the skeleton and found a keycard")
            keycard = True

        elif a.upper() == "COMPUTER" or a.upper() == "COM":
            print("You inspected the computer. It says that it requires a keycard and a private key to start")
            if keycard == True and private_key == True:
                print("You insert the keycard and the private key into the computer")
                print("The computer slowly boots up")
                print("The computer gives you the option to restart the backup generator. You press ok and soon you hear the electronic door opening")
                escape_1 = True
                break

        elif a.upper() == "LIGHTBOX" or a.upper() == "LIGHT":
            print("You inspected the breaker box. It seems that all of the switches aren't working at the moment.")
            print("Fret not! You do notice a sticky note with a string of random numbers and letters. It is labeled as the private key")
            print("You got the private key!")
            private_key = True
        elif a == "1":
            print("You inspect box #1 and you find nothing :(")
        elif a == "2":
            print("You inspect box #2 and you find a small key. I wonder what it's used for")
            small_key = True
        else:
            print("That's not right!")
        a = input("""What do Inspect?\n The \'skeleton\' \n box \'1\' \n box \'2\'\n The\'Light\'box \n The\'door\'\n or the \'Computer\'?: """)
    print("You escaped room 1!")
    return True

def room_2():
    escape_2 = False
    riddle_count = 0
    riddle_list = ["moss", "crow", "lightning"]
    print("you walk into the next room and spot 3 screens and a hanging light. What do you inspect?")
    while escape_2 == False:
        c = input("What do you inspect?: The 'Light', Screen #'1', #'2', #'3', or the Door?: ")
        if c.upper() == "LIGHT":
            print("You inspect the hanging light. It has long frayed wires leading up to open ceiling boards. Do you want to climb it?")
            climb_or_no = input("Do you want to climb it?: ")
            if climb_or_no.upper() == "YES":
                print("Ow! You were electrocuted. You're lucky to survive! Did you forget that you turned on the backup generator?")
            else:
                print("You feel unsettled by the hanging light and decide to leave it alone.")
        elif c == "1":
            print("It's a riddle")
            print("Hidden in shadows; Bathed in light. Which ever direction it heads is right.")
            answer_1 = input("Enter your answer: ")
            if answer_1.lower() == riddle_list[0]:
                riddle_count += 1

        elif c == "2":
            print("It's a riddle")
            print("Sharp as a nail, soft as a feather. Reminds people of rainy weather.")
            answer_2 = input("Enter your answer: ")
            if answer_2.lower() == riddle_list[1]:
                riddle_count += 1
        elif c == "3":
            print("It's a riddle")
            print("Fickle in sight, strong in spirit. You often see it before you hear it.")
            answer_3 = input("Enter your answer: ")
            if answer_3.lower() == riddle_list[2]:
                riddle_count += 1
        elif c.upper() == "DOOR":
            print("You head over to the door. It looks like it needs the riddles to be answered to open.")
            if riddle_count == 3:
                    print("You got them all right!")
                    escape_2 = True
            else:
                print("you haven't gotten the riddles right yet.")
    print("You escaped room 2!")
    return True

def room_3 ():
    print("You enter room 3 and see a series of buttons on the floor.")
    print("It seems that you need to get 3 buttons correct to continue.")
    escape_3 = False
    correct_count = 0
    while escape_3 == False:
        e = random.randint(1,3)
        f = int(input("Within the range of 1 - 3, which number will you pick?: "))
        if f == e:
            print("You got it correct!")
            correct_count += 1
            if correct_count == 3:
                print("It seems like the button puzzle is finished.")
                escape_3 = True
        else:
            print("That seems to be the wrong number...")
    print("You escaped room 3!")
    return True

def room_4 ():
    global small_key
    print("You go into room for and notice that it is damp on the floor. Suddenly, the door behind you slams closed and water start filling the room.")
    print("There is a door at the other side of the room. You rush over to the door and try to open it but it won't budge. There is a built in scanner that says it needs an item.")
    for i in range (3):
        urgent_input = input("What do you want to scan?: ")
        if small_key == True:
            print("You open the door with the small key you got from earlier.")
            return True
        if urgent_input:
            print("That won't work!")
    else:
        print("you were not able to get out of the room and drowned :(")
        return False

def main ():
    success = False
    print("""You are a travelling alien, going from planet to planet to find your lost sibling. 
          You come across a deserted planet on one of you travels and decide to stop to take a rest and maybe find some supplies.
           While landing, you spot a ship in the distance and decide to dock there.
           """)
    print("""After docking, you notice that the ship seems deserted. You decide to look around in the ship to see 
    if anyone is there and if not, maybe even find something of value. You look in a random room and are greeted with a skeleton.
    Thoroughly freaked out, you try to leave the way you came but the door is now jammed!""")
    print("After looking around a bit more, you see a few things that look interesting.")
    c_1 = input("""What do Inspect?\n The \'skeleton\' \n box \'1\' \n box \'2\'\n The\'Light\'box \n or the \'Computer\'?: """)

    while success == False:
        if room_1(c_1):
            if room_2():
                if room_3():
                    if room_4():
                        success = True
                    else:
                        print('You have died :(')
            else:
                print('You have died :(')
main()
