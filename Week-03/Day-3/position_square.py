from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
def square_drawer(x,y):
    box = canvas.create_rectangle(x, y, x+50, y+50, fill='lime green')

square_drawer(1,1)
square_drawer(100,100)
square_drawer(160,160)
root.mainloop()