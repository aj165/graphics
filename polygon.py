from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import time
from math import cos as cos
from math import sin as sin


def init():
    glClearColor(0.75, 0.75, 0.75, 0.75)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)


l = []
a = int(input("Enter number of vertices "))
for i in range(0, a):
    x = int(input("Enter x coordinate"))
    y = int(input("Enter y coordinate"))
    l.append([x, y])


def points():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    d=l
    #glFlush()
    polygon(d)
    ddaline([-250,0],[250,0])


def ddaline(p, q):
    glBegin(GL_POINTS)
    x1, y1 = p
    x2, y2 = q
    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) > abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    for k in range(int(steps)):
        x1 += xinc
        y1 += yinc
        glVertex2f(x1, y1)
    glEnd()
    glFlush()


def polygon(vertices):
    for j in range(len(vertices)):
        ddaline(vertices[j], vertices[(j + 1) % len(vertices)])


def translate(tx,ty,vertices):
    for vertex in vertices:
        vertex[0]+=tx
        vertex[1]+=ty
    return vertices


def move(button, state, x, y):
    if (button == GLUT_LEFT_BUTTON and state == GLUT_UP):
        animate()

def animate():
    for i in range (5):
        refresh()
        polygon(translate(10,0,l))
        time.sleep(1)

def refresh():
    glClear(GL_COLOR_BUFFER_BIT)
    ddaline([-250,0],[250,0])



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"fiufasigf")
    glutDisplayFunc(points)
    glutMouseFunc(move)
    init()
    glutMainLoop()


main()
