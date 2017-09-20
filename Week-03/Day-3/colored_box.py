from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
lime_box = canvas.create_rectangle(50, 50, 100, 100, fill='lime green')
top_line = canvas.create_line(50, 50, 100, 50, fill='red')
bottom_line = canvas.create_line(50, 100, 100, 100, fill='blue')
left_line = canvas.create_line(50, 50, 50, 100, fill='black')
right_line = canvas.create_line(100, 50, 100, 100, fill='purple')

root.mainloop()