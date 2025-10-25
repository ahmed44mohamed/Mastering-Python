bmi = 84 / 1.65 ** 2

print (bmi)

print (int(bmi))

print (round(bmi)) # 31

# round (number, digits)

print (f"With 2 digit: {round(bmi, 2)}")
print (f"With 3 digit: {round(bmi, 3)}")

score = 0 # 0

score += 3 # 3

score -= 1 # 2

score *= 2 # 4

score /= 2 # 2

score **= 2 # 4

score //= 2 # 2

# mix string and different data type use f-string

height = 1.8

is_winning = True

print (f"Your score is {int(score)}, your height is {height}. You are winning is {is_winning}")