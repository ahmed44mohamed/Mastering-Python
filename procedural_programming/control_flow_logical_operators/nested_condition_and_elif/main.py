# Nested condition & elif
# if condition:
#   if condition:
#       do this
#   else:
#       do this
# else:
#   do this

print ("Welcome to the rollercoaster!")
height = int(input("What is your height in CM? "))

if height >= 120:
    print ("You can ride the rollercoaster")
    age = int (input("What is your age? "))
    if age <= 18:
        print ("Your should pay 7$")
    else:
        print ("You should pay 12$")
else:
    print ("Sorry, You can't. You have to grow taller before you can ride.")

# elif

print ("Welcome to the rollercoaster!")

height = int(input("What is your height in CM? "))

if height >= 120:
    print ("You can ride the rollercoaster")
    age = int (input("What is your age? "))
    if age <= 12:
        print ("You should pay 5$")
    elif age <= 18:
        print ("You should pay 7$")
    else:
        print ("You should pay 12$")
else:
    print ("Sorry, You can't. You have to grow taller before you can ride.")