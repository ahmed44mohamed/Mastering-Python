

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print ("Welcome to the PyPassword Generator!")
n_letters = int (input ("How many letters would you like in your password? "))
n_symbols = int (input ("How many symbols would you like? "))
n_numbers = int (input ("How many numbers would you like? "))

password_list = []

for num in range (0, n_letters):
    password_list += random.choice(letters)

for num in range (0, n_symbols):
    password_list += random.choice(symbols)

for num in range (0, n_numbers):
    password_list += random.choice(numbers)

easy_password = ""

for char in password_list:
    easy_password += char

print (f"Easy password is {easy_password}")

hard_password = ""

random.shuffle(password_list)

for char in password_list:
    hard_password += char

print (f"Hard password is {hard_password}")

