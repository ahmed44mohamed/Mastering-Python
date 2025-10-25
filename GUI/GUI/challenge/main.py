# positions using grid challenge

import tkinter

window = tkinter.Tk ()

window.title ("Challenge")
window.minsize (width= 1000, height= 1000)
window.config (padx= 30, pady= 30)

label = tkinter.Label (text= "This is a label")
label.grid (column= 0, row= 0)

button = tkinter.Button (text= "Click here")
button.grid (column= 1, row= 1)

new_button = tkinter.Button (text = "New Button")
new_button.grid (column= 2, row = 0)


input = tkinter.Entry ()
input.grid (column= 3, row= 2)

window.mainloop ()