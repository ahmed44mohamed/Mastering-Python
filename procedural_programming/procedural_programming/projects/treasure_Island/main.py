print ("Welcome to treasure Island.\nYour mission is to find the treasure.")
choose_1 = input ("You 're at a cross road. Where do you want to go?\n\t\tType \"left\" or \"right\"\n").lower()
if choose_1 == "right":
    print ("Game over.")
elif choose_1 == "left":
    print ("You 've come to a lake. There is an island in the middle of the lake")
    choose_2 = input ("\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if choose_2 == "swim":
        print ("Game over.")
    elif choose_2 == "wait":
        choose_3 = input ("You arrive at the island unharmed.\nThere is house with 3 doors. One red, One blue, One Yellow.\n Which color do you choose? ").lower()
        if choose_3 == "yellow":
            print ("YOU WIN!")
        else:
            print ("Game Over")
    else:
        print ("You typed wrong!!!")
else:
    print ("You typed wrong!!!")