#gemaakt door: Reza van Wegberg en Lara Mollaoglu
def introductie():
    print ("This is a quick decision game where bad answers can lead to a bad ending. You're only given 1 chance..")

introductie()
level = input ("\nAlright you're in a dungeon while being level 3 you see an orc that is level 18\nAre you gonna fight it? y/n: ")
if level == "y":
    print("\nYou shouldn't have done that. you are now in the injury state \n A random citizen should heal you know if you want to continue\n")
    level1= input ("\nYou found a farmer who wanted to help you.\n\nAre you gonna accept it? y/n: ")
    if level1 == "y":
        level2 = input("You feel replenished\nYou see bandits robbing someone, are you going to help y/n: ")
        if level2 == "y":
            print("You thought that you were a hero.\nBut there were way too many for you to handle.\nBAD ENDING!. You died.")
        elif level2 == "n":
            print("They saw you running away, and they shot you down. \nBAD ENDING!. You died.")
    elif level1 == "n":
        print("\n You chose a bad answer. You should have accepted it")
        level3=input("""You don't feel so good\nBut you're lucky you found a teleport scroll\n=================
town
forrest
castle
=================\nWhich allows you to teleport to one of these places.\nPick wisely.""")

        if level3 == "town":
            print ("You teleported to the town. You found a doctor.\nHe helped you and you became his pupil.\nPACIFIST ENDING!. you won!")
        elif level3 == "forrest":
            print ("You teleported to the forrest. But sadly a war was active. And you got teleported right in the middle of it.\nSadly enough you died!\n BAD ENDING!.")
        elif level3 == "castle":
            print ("You teleported to the castle. Wrong choice the king thought that you were a spy.\nYou got put into prison and then you got executed.\nBAD ENDING! ")

elif level == "n":
    print("\nYou escaped and found a lovely village near the river.")
    print ("""=====
Village
River
=====""")
    level6 = input("Are you going to the village or to the river?: ")
    if level6 == "village":
        print ("""You see many shops.\n=====\nFlowershop\nClothingshop\nBlack Smith\n=====""")
        level7 = input("Which shop would you like to visit?: ")
        if level7=="flowershop":
            print("You saw a lovely grandma and she gave you a beautiful flower bouquet\nGOOD ENDING!")
        elif level7 =="clothingshop":
            print ("You sadly didn't have enough money for new clothes.\nSo you got caught for stealing something and got kicked out of the shop.\nBAD ENDING!")
        elif level7 == "black smith":
            print ("The middle aged man treated you like a friend. You got a free weapon and you also got the chance to work there.\nGOOD ENDING!")
    elif level6 =="river":
        print("You see a woman , 2 children and a buffed man. Which one would you like to have a talk with? ")
        print ("""==========
woman
2 children
buffed man
==========""")
        level8 = input ("Which of the following people would you like to talk to? ")
        if level8 =="woman":
            print ("You had a lovely chat with her and you both felt the connection between each other\n GOOD ENDING!")
        elif level8 =="2 children":
            print ("The 2 children had a very nice evening with you and they wanted to play with you more.\nGOOD ENDING!")
        elif level8 =="buffed man":
            print ("That wasn't a very nice chat he drowned you. And you died\nBAD ENDING!")
    

else:
    print ("Invalid option") 