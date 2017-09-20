from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
def box_drawer(z):
    box = canvas.create_rectangle(150-(z/2), 150-(z/2), 150+(z/2), 150+(z/2),)
box_drawer(50)
box_drawer(100)
box_drawer(200)
root.mainloop()