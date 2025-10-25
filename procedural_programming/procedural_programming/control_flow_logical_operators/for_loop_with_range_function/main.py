# for loop with range

for num in range (1, 10): # not include last digit (10)
    print (num)

print ("---")

for num in range (1, 11, 2): # This will increase by 2 -->  1 3 5 7 9
    print (num)

print ("---")
# Sum of all number from 1 to 100

sum = 0

for num in range (1, 101):
    sum += num

print (f"The sum of numbers from 1 to 100 = {sum}")