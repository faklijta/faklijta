from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
def line_drawer(x,y):
    green_line1 = canvas.create_line(x, y, 150, 150, fill='light sea green')

line_drawer(5,5)
line_drawer(150,290)
line_drawer(290,0)
root.mainloop()