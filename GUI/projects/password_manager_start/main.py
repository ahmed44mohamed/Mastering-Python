# Importing
import tkinter as tk
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password ():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice (letters) for _ in range(randint(8, 10))]

    symbols_list = [choice (symbols) for _ in range(randint(2, 4))]

    numbers_list = [choice (numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + symbols_list + numbers_list

    shuffle(password_list)


    password= "".join (password_list)

    entry_password.insert(0, password)

    pyperclip.copy (password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save ():
    # Take the inputs
    input_website = entry_website.get ()
    input_email = entry_usr_name.get ()
    input_password = entry_password.get ()

    is_ok_1 = input_website == "" or input_email == "" or input_password == ""

    if is_ok_1:
        messagebox.showinfo("Oops", "Please don't leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel (title= input_website, message= f"email: {input_email}\nPassword: {input_password}")

        if is_ok:
            with open ("data.txt", "a") as file:
                file.write (input_website + " | " + input_email + " | " + input_password + "\n")

            entry_password.delete (0, tk.END)
            entry_usr_name.delete (0, tk.END)
            entry_website.delete (0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk ()

window.title ("Password manager")

canvas = tk.Canvas (width= 200, height= 200)

image = tk.PhotoImage (file= "./logo.png")
canvas.create_image (100, 100, image=image)

window.config (padx= 50, pady= 50)
canvas.grid (column= 1, row= 0)

label = tk.Label (text= "Website:")
label.grid (column= 0, row= 1)

entry_website = tk.Entry (width= 35)
entry_website.grid (column= 1, row= 1, columnspan= 2)
entry_website.focus ()

label_2 = tk.Label (text= "Email/Username:")
label_2.grid (column= 0, row= 2)

entry_usr_name = tk.Entry (width= 35)
entry_usr_name.grid (column= 1, row= 2, columnspan= 2)
entry_usr_name.insert (0, "name@gmail.com")

label_3 = tk.Label (text= "Password:")
label_3.grid (column= 0, row= 3)

entry_password = tk.Entry (width= 21)
entry_password.grid (column= 1, row= 3)

button = tk.Button (text= "Generate password", command= generate_password)
button.grid (column= 2, row= 3)

button_add = tk.Button (text= "Add", width= 36, command= save)
button_add.grid(column= 1, row= 4, columnspan= 2)

window.mainloop ()



