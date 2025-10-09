# Importing
import tkinter


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk () # Window
window.title = "Password manager"
window.config (padx= 20, pady= 20)
# window.minsize (width= 400, height= 400)

canvas = tkinter.Canvas (width= 200, height= 200) # Canvas
lock_photo = tkinter.PhotoImage (file= "./projects/password_manager_start/logo.png")
canvas.create_image (100, 100, image= lock_photo)
canvas.pack ()

# Keep it on
window.mainloop ()