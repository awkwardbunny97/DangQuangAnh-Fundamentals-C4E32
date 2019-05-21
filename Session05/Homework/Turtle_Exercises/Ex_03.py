from turtle import *

def draw_square(length,line_color):
    color(line_color)
    for i in range(4):
        forward(length)
        left(90)
    mainloop()

draw_square(97,'red')
