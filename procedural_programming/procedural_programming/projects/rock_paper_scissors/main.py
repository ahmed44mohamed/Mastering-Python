import random

chooses = ["rock", "paper", "scissors"]

user_choose = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors  "))
computer_choose = random.randint(0, 2)

print (f"You choose {chooses[user_choose]}")
print (f"Computer choose {chooses[computer_choose]}")

if user_choose == computer_choose:
    print ("Draw")
elif (user_choose == 0 and computer_choose == 2) or (user_choose == 1 and computer_choose == 0) or (user_choose == 2 and computer_choose == 1) :
    print ("You win")
else:
    print ("You lose")