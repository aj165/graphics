from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys


x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

def init():
    glClearColor(0.75, 0.75, 0.75, 0.75)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)



def lines():
    global x1,x2,y1,y2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    a=[x1,y1]
    b=[x2,y2]
    ddaline(a,b)

def ddaline(a,b):
    glBegin(GL_POINTS)
    x1,y1=a
    x2,y2=b
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
