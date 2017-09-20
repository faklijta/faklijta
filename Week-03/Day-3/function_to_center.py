from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def line_drawer(x1, y1):
    line = canvas.create_line(x1, y1, 150, 150)

line_drawer(0, 0)
i = 0
while i < 300:
    line_drawer(0, i)
    line_drawer(i, 0)
    line_drawer(300, i)
    line_drawer(i, 300)
    i +=20
root.mainloop()