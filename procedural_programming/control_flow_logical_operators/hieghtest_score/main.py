student_score = [95, 120, 134, 88, 102, 176, 150, 99, 110, 143, 160, 85, 132, 190, 170, 105, 115, 140, 155, 180]

total_exam_score = sum(student_score)

print (f"Total score using sum function = {total_exam_score}")

# You can make it by loop

sum = 0

for score in student_score:
    sum += score

print (f"Total score using for loop = {sum}")

print (f"Max score using max function = {max(student_score)}")

max = student_score[0]

for score in student_score:
    if score > max:
        max = score


print (f"Max score using for loop = {max}")