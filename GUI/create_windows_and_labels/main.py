import tkinter

# Crete Object
window = tkinter.Tk ()

# Change title
window.title ("My first GUI Program")

# Size
window.minsize (width= 1000, height= 600)

# Create label
my_label = tkinter.Label (text= "This is a Label", font= ("Arial", 24, "bold"))
# my_label.pack (expand= True)
my_label.pack (side= "top")

# Change text
my_label ["text"] = "New text"
# or
my_label.config (text= "NEW TEXT")

# To keep it open
window.mainloop ()

