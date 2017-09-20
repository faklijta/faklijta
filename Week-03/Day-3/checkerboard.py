from tkinter import *

root = Tk()

canvas = Canvas(root, width='320', height='320')
canvas.pack()

# fill the canvas with a checkerboard pattern.
def checkboard():
    size = 40
    x1 = 0
    y1 = 0
    x2 = size
    y2 = size
    for i in range(0, 320):
        for j in range(0, 320):
            if i % 2 == 0:
                if j % 2 == 0:
                    square_black = canvas.create_rectangle(x1, y1, x2, y2, fill = "black")
                    x1 += size
                    x2 += size
                else:
                    square_white = canvas.create_rectangle(x1, y1, x2, y2, fill = "white")
                    x1 += size
                    x2 += size
            else:
                if j % 2 == 0:
                    square_white = canvas.create_rectangle(x1, y1, x2, y2, fill = "white")
                    x1 += size
                    x2 += size
                else:
                    square_black = canvas.create_rectangle(x1, y1, x2, y2, fill = "black")
                    x1 += size
                    x2 += size
        x1 = 0
        x2 = x1 + size
        y1 += size
        y2 += size 
checkboard()
root.mainloop()