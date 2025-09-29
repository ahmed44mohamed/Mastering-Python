import pandas

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

student_data_frame = pandas.DataFrame (student_dict)

print (student_data_frame)
print (type (student_data_frame))

print ("============================================================================")

# Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows ():
    if row.student == "Angela":
        print (row.score)

