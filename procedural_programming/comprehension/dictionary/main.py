# Syntax

# new_dict_name = {new_key: new_value for item in list}

# new_dict_name = {new_key: new_value for (key, value) in dict.items ()}

# new_dict_name = {new_key: new_value for (key, value) in dict.items () if test}

from random import randint

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_score = {name : randint (1, 100) for name in names}

print (students_score)

print ("------------------------------------")

passed_student = {name : scores for (name, scores) in students_score.items () if scores >= 60}

print (passed_student)
