import turtle
import math
import colorsys

turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)
turtle.tracer(0, 0)  


def heart_x(t):
    return 16 * math.sin(t) ** 3

def heart_y(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)


points = []
for i in range(360):
    t = math.radians(i)
    x = heart_x(t) * 10
    y = heart_y(t) * 10
    points.append((x, y))

n = len(points)
hue = 0

for frame in range(500): 
    turtle.clear()
    for i in range(0, n, 4):
        j = (i + frame) % n
 
        rgb = colorsys.hsv_to_rgb((hue + i / n) % 1.0, 1, 1)
        r, g, b = [int(255 * val) for val in rgb]
        turtle.pencolor(r, g, b)
        turtle.penup()
        turtle.goto(points[i])
        turtle.pendown()
        turtle.goto(points[j])
    hue += 0.005
    turtle.update() 

turtle.done()
