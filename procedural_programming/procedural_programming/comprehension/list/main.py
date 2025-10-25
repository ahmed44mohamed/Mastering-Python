# List comprehension
# new_list_name = [<process_to_get_new_list> for <each_item_name> in <old_list_name>]

numbers = [1, 2, 3, 4]

new_numbers = [1 + n for n in numbers]

print (new_numbers)

# You can work with other comprehension like: string

name = "Ahmed"

new_name = [letter for letter in name]

print (new_name)

# With range

old_range = range (1, 5)

new_range = [n * 2 for n in old_range]

print (new_range)

# Conditional List comprehension

# new_list_name = [<process_to_get_new_list> for <each_item_name> in <old_list_name> if test]

letters = ["aaa", "bbbb", "ccccc", "dddddd"]

short_letters = [letter for letter in letters if len (letter) < 5]

print (short_letters)

upper_case_letters = [letter.upper () for letter in letters if len (letter) >= 5]

print (upper_case_letters)