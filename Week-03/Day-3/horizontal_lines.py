from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.
def line_drawer(x,y):
    green_line1 = canvas.create_line(x, y, x+50, y, fill='light sea green')

line_drawer(5,5)
line_drawer(150,100)
line_drawer(200,5)

root.mainloop()