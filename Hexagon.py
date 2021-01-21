import turtle as t
import time

def spiral(sides, trun, color, width):
    pen = t.Turtle()
    pen.color(color)
    pen.width(width)
    pen.speed(0)
    for n in range(sides):
        pen.forward(n)
        pen.right(trun)


spiral(150, 45, "cyan", 5)
time.sleep(10)