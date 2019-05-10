from turtle import *

color("red")

for i in range(4):
    for v in range(2):
        left(120)
        forward(100)
        right(60)
        forward(100)
        right(240)
    right(90)

mainloop()