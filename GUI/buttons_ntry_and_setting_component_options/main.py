# Importing Section
import tkinter

# Functions section
def button_clicked ():
    new_text = input.get ()
    label.config (text= new_text)

# Make object
window = tkinter.Tk ()

# Change the title
window.title ("GUI program")

# Set min size for window
window.minsize (width= 1000, height= 700)

# Make a label
label = tkinter.Label (text= "This is a Label", font= ("Arial", 24, "bold"))

# Put the label on the top
label.pack (side= "top")

# Change the text in the label
label.config (text= "Text change one") # Way one
label ["text"] = "Text change two" # way two like in dictionary

# Create button
button = tkinter.Button (text= "Click here")

# Put the label on the top
button.pack (side= "top")

# Make button work by change the text in the label
button.config (command= button_clicked)

# Entry = input
input = tkinter.Entry (width= 20)
input.pack () # Yeah, The default in the top center

# .get () ===> return the input as string
typed_text_in_entry = input.get ()

# Keep program on
window.mainloop ()