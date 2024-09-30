name = input("enter your name : ")
print("welcome ",name," lets go in the ADVENTURE :) ")

#story start
print("you lost in a jungule. now you try to find the path .")
ans=input("you are on a dry road. the road is end . you can go left or right: ").lower()
print(".........................")
if(ans=="left"):
    print("you see a cave and hear a watter fall sound. \n what you do now?\ntake rest in cave or follow the watter sound")
    ans = input("if you take rest write-> cave\nif you follow the sond write-> water").lower()
    print(".........................")
    if(ans=="cave"):
        print("a tiger live in the cave . he eat you . ...:(")
    elif(ans=="water"):
        print("you follow the sound . then you find out the water fall .\n sudden you see it is a touest spot \n..... you win ..")
    else:
        print("you losssee the game")

elif(ans == "right"):
    print("you see a river. \n what you do now?\n walking beside the river  or swime in the river to the other side ")
    print(".........................")
    ans = input("wakling beside river-> walk\n swime in river-> swime").lower()
    if(ans=="walk"):
        print("walking and find a big road  .. take a lift to go home . you win")
    elif(ans=="swime"):
        print("crocodile live in the river.\n he eat you \n you lossee")
    else:
        print("you losssee the game")
else:
    print("you losssee the game")