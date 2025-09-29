# Importing Section
import tkinter

# Make object
window = tkinter.Tk ()

# Change the title
window.title ("GUI program")

# Set min size for window
window.minsize (width= 1000, height= 700)

# Make a label
label = tkinter.Label (text= "This is a Label", font= ("Arial", 24, "bold"))

# Change the position ny place ()
label.place (x= 100, y= 200)

# Change using grid ()
label.grid (column= 0, row= 0)

# Change the text in the label
label.config (text= "Text change one") # Way one
label ["text"] = "Text change two" # way two like in dictionary

# Create button
button = tkinter.Button (text= "Click here")
button.grid (column= 1, row= 1)

# Entry = input
input = tkinter.Entry (width= 20)
input.grid (column= 2, row= 2)

# .get () ===> return the input as string
typed_text_in_entry = input.get ()

# Keep program on
window.mainloop ()