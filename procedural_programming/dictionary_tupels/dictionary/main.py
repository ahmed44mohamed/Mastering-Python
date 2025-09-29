# Dictionary

# Syntax

# name_dictionary = { 
# Key 1 : Value 1,
# key 2 : value 2,
# Key 3 : value 3
# }

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print (programming_dictionary["Bug"])
print (programming_dictionary["Function"])

print ("----------------------------- Before any update -----------------------------")

# Add an item to the dictionary

programming_dictionary ["Loop"] = "The action of doing something over and over again."

print (programming_dictionary)

print ("----------------------------- After Add Loop item -----------------------------")

# Edit an item in a dictionary

programming_dictionary ["Bug"] = "A moth in your computer"

print (programming_dictionary["Bug"])

print ("----------------------------- After edit Bug item -----------------------------")

# Loop through a dictionary  --> It will gives us the keys

print ("-----------------------------  Loop through a dictionary -----------------------------")

for key in programming_dictionary:
    print (key)
    print (programming_dictionary[key])

# Wipe an existing dictionary

programming_dictionary = {}

print (programming_dictionary)

