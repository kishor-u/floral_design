import turtle
import math
import random
pensize = 2
window = turtle.Screen()
window.bgcolor('black')

Shape1 = turtle.Turtle()
Shape1.speed(0.1)
Shape1.color('brown')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        t.pensize(pensize)
        size=size-4
def drawShape(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawShape(Shape1,130,10)


Shape2 = turtle.Turtle()
Shape2.speed(0)
Shape2.color('violet')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        t.pensize(pensize)
        size=size-10
def drawShape(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawShape(Shape2,130,10)


Shape3 = turtle.Turtle()
Shape3.speed(0)
Shape3.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        t.pensize(pensize)
        size=size-5
def drawShape(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawShape(Shape3,130,10)


Shape4 = turtle.Turtle()
Shape4.speed(0)
Shape4.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(2):
        t.circle(size)
        size=size-pensize
def drawShape(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawShape(Shape4,130,10)


window.exitonclick()
