import tkinter

window = tkinter.Tk ()
window.title ("Learn Canvas widget")
window.config (padx= 100, pady= 50)
canvas = tkinter.Canvas (width= 200, height= 224)
tomato_img = tkinter.PhotoImage (file= "./canvas_widget/tomato.png")
canvas.create_image (103, 112, image= tomato_img) # In the center of the screen
canvas.create_text (103, 130, text= "00:00", fill= "white")
canvas.pack ()

window.mainloop ()