from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
x4 = int(input("Enter x4: "))
y4 = int(input("Enter y4: "))
xc = int(input("Enter x coordinate of centre of circle"))
yc = int(input("Enter y coordinate of centre of circle"))
r = int(input("Enter radius of circle"))


def init():
    glClearColor(0.75, 0.75, 0.75, 0.75)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)


def lines():
    global x1, x2, y1, y2, x3, y3, xc, yc, r
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    a = [x1, y1]
    b = [x2, y2]
    c = [x3, y3]
    d = [x4, y4]
    e=[xc,yc,r]
    ddaline(a, b)
    ddaline(b, c)
    ddaline(b, d)
    circle(xc,yc,r)


def ddaline(a, b):
    glBegin(GL_POINTS)
    x1, y1 = a
    x2, y2 = b
    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) > abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    for i in range(steps):
        x1 += xinc
        y1 += yinc
        glVertex2f(x1, y1)
    glEnd()
    glFlush()


def circle(xc,yc,r):
    glBegin(GL_POINTS)
    x, y = 0, r
    p = 1 - r
    while (x < y):
        x += 1
        if (p < 0):
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x - 2 * y - 1
        glVertex2f(x + xc, y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        glVertex2f(-x + xc, -y + yc)
        glVertex2f(y + xc, x + yc)
        glVertex2f(-y + xc, x + yc)
        glVertex2f(y + xc, -x + yc)
        glVertex2f(-y + xc, -x + yc)
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"test")
    glutDisplayFunc(lines)
    init()
    glutMainLoop()


main()
