def add (*arg):
    sum = 0
    for n in arg:
        sum += n

    print (type (arg)) # Tuple

    return sum

print (add (1, 2, 4, 1)) # 1 + 2 + 4 + 1 = 8
print (add (1, 3)) # 1 + 3 = 4
