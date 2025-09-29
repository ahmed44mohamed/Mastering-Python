# if condition_1:
#   do A
# if condition_2:
#   do B
# if condition_3:
#   do C


print ("Welcome to the rollercoaster!")

height = int(input("What is your height in CM? "))
bill = 0
if height >= 120:
    print ("You can ride the rollercoaster")
    age = int (input("What is your age? "))
    if age <= 12:
        print ("Child tickets are 5$")
        bill += 5
    elif age <= 18:
        print ("Youth tickets are 7$")
        bill += 7
    else:
        print ("Adult tickets are 12$")
        bill += 12

    want_photo = input ("Do you want to have a photo ticket? Type y for yes and n for no. ")

    if want_photo == "y":
        bill += 3
    
    print (f"The bill = {bill}$")

else:
    print ("Sorry, You can't. You have to grow taller before you can ride.")