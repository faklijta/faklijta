from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
rectangle = canvas.create_rectangle(10, 10, 55, 55, fill='lime green')
rectangle = canvas.create_rectangle(100, 100, 135, 135, fill='yellow')
rectangle = canvas.create_rectangle(45, 45, 65, 65, fill='red')
rectangle = canvas.create_rectangle(145, 145, 300, 300, fill='white')

root.mainloop()