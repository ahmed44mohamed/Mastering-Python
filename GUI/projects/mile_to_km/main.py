# Importing Section
import tkinter

# Functions Section
def miles_to_km ():
    """
    This function calculate from miles to Km

    """
    miles = float (usr_input.get ())
    km = miles * 1.609
    num_in_km_label.config (text= f"{km}")


def show_new_value_in_km (n):
    num_in_km_label.config (text= f"{n}")

# Set up the window
window = tkinter.Tk ()
window.title("Mile to Kilometers program")
window.config (padx= 100, pady= 100)

# Create the labels
FONT = ("Arial", 20, "bold")
miles_label = tkinter.Label (text= "Miles", font= FONT)
is_equal_label = tkinter.Label (text= "is equal to", font= FONT)
num_in_km = 0
num_in_km_label = tkinter.Label(text= "0", font=FONT)
km_label = tkinter.Label (text= "Km" ,font= FONT)

# Create Entry
usr_input = tkinter.Entry ()

# create button
button = tkinter.Button (text= "Calculate", command= miles_to_km)

# Set up
miles_label.grid (row= 0, column= 2)
miles_label.config (padx= 10, pady= 10)
is_equal_label.grid (row= 1, column= 0)
km_label.grid (row= 1, column= 2)
num_in_km_label.grid (row= 1, column= 1)

usr_input.grid (row= 0, column= 1)

button.grid (row= 2, column= 1)

# Keep it on
window.mainloop ()


