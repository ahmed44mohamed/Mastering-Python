# You can store different data types in a list in Python the only thing is matter is a syntax
items = [1, 2.5, 'c', "Hello", True]

names = ["Ahmed", "Bassam", "Moaz"]

# Print items by index
print (f"first element is {names[0]}") # Ahmed
print (f"last element by negative index is  {names[-1]}") # Moaz

names[0] = "Mohamed" # change first item to mohamed
print (f"First element after update is {names[0]}") # Mohamed

names.append("Ibrahim") # To add one items for out list
print (f"Add element for the list {names}")

names.extend(["Aliaa", "Zahra", "Hagar"]) # To add list (more than one item)
print(f"Addition list {names}")

names.insert(2, "AMR") # add item by position (index)
print(f"Add element for known position by index {names}")

names.remove("AMR") # Delete item by value
print(f"Remove element by value {names}")

names.pop(0) # remove item by index
print(f"Remove element by index {names}")

names.clear() # remove all items
print (names)

# The index() function returns the index of the first occurrence of a specified value in the list. It can also take optional start and end parameters to search within a specific range. If the value is not found, it raises a ValueError.
names.extend(["Mohamed", "Ahmed", "Bassam", "Ali", "Ahmed", "Aliaa", "Ahmed"])
print(names.index("Ahmed")) # 1
print(names.index("Ahmed", 2)) # 4
print(names.index("Ahmed", 4, 6)) # 4

print(names.count("Ahmed")) # 3

names.sort() # Sorts the list in ascending
print(names)

names.sort(reverse=True)
print(names)

names.sort(key=len)
print(names)

names.reverse()
print(names)

new_list = names.copy()
print (new_list)

new_list.append("FFFFFFF")
print (new_list)

