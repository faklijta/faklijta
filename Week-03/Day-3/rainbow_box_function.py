from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
rainbow_colors = ["pink","red", "orange", "yellow", "green", "blue"]
def box_drawer(size, colors):
    start_point = 150 - (size / 2)  
    end_point = 150 + (size / 2)  
    square = canvas.create_rectangle(start_point, start_point, end_point, end_point, fill = colors)

for i in range(len(rainbow_colors)):
    side = 300-i*50
    box_drawer(side,rainbow_colors[i])
root.mainloop()