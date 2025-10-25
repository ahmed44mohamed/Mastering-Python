# To open
file = open ("./procedural_programming/open_read_and_write_to_files/my_file.txt")

# To take the text
contents = file.read ()

# Print it out  
print (contents)

# To close
file.close ()

print ("\n--------------------------------")

# Another way 
with open ("./procedural_programming/open_read_and_write_to_files/my_file.txt") as file:
    contents = file.read ()
    print (contents)

print ("\n--------------------------------")
# To write in the file

# with open ("my_file.txt", mode= "w") as file:
#     file.write ("\nNew line here.")  =====> This mode will delete all the text before.

with open ("./procedural_programming/open_read_and_write_to_files/my_file.txt", mode= "a") as file:
    file.write ("\nNew line here.")