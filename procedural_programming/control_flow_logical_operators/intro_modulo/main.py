# Modulo operator --> %

print (10 % 5) # 0

print (10 % 3)

# 10 / (3) = (3).33333333333333333
# 3 * 3 = 9
# 10 - 9 = 1

print (11 % 3)
# 11 / 3 = 3.666666667
# 3 * 3 = 9
# 11 - 9 = 2

print ("Check number odd or even")
num = int(input("Number: "))
if num % 2 == 0:
    print ("Even")
else:
    print ("Odd")