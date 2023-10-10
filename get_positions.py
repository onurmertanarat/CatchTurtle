from turtle import *
import turtle as tur


def pos(event):
    a, b = event.x, event.y
    print('{}, {}'.format(a, b))


ws = tur.getcanvas()
ws.bind('<Motion>', pos)

tur.done()
