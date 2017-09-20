from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

step = 20
width = 300

def line_drawer_green(x, y):
    line = canvas.create_line(x, y, y, width/2,  fill = "green")

def line_drawer_purple(x, y):
    line = canvas.create_line(y, x, width/2, y, fill = "purple")

i = 0
while i < 140:
    i += step
    line_drawer_green(0,i)

j = 0
while j < 140:
    j += step
    line_drawer_purple(0, j)

line_drawer_green(0, step)
line_drawer_purple(0, step)

root.mainloop()