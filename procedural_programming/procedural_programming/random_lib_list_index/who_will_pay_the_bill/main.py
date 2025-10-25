import random

print ("======== { way 1 } ===========")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_num = random.randint(a = 0, b = 4)

print (f"The person will pay is {friends[random_num]}")

print ("======== { way 2 } ===========")

random_num_2 = random.choice(friends)

print (f"The person will pay is {random_num_2}")