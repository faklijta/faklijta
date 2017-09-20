from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw the canvas' diagonals in green.
green_line1 = canvas.create_line(0, 0, 300, 300, fill='light sea green')
green_line1 = canvas.create_line(0, 300, 300, 0, fill='light sea green')

root.mainloop()