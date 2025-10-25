import random
import my_module

random_num = random.randint(1, 10) # random.randint(a, b) Return a random integer such that a <= N <= b

print (f"Random number between 1 and 10 : {random_num}")

print (f"My favorite number is {my_module.my_fav_num}")

# random number between 0 and 1
# this will return num ---> 0 <= N < 1 not include 1

random_num_0_1 = random.random()

print (f"Random number between 0 and 1 is {round(random_num_0_1, 2)}")

# random float number between 0 and 10 but not include 10

random_num_f_0_10 = random.random() * 10

print (f"Random number between 0 and 10 is {round(random_num_f_0_10, 2)}")

# random float number
# random float number between 1  and include 1 and 10
random_float_number = random.uniform(1, 10)

print (f"Random float number between 1 and 10 is {round(random_float_number, 2)}")

print ("-------------------------practice-----------------------------------------")

r_num = random.randint(a=0,b=1)

if r_num == 0:
    print("Heads")
else:
    print ("Tails")