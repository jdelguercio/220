import graphics

# my_point = graphics.Point(50,70)
# point_a = graphics.Point(70,90)
# point_a.move(10,0)
#
# window = graphics.GraphWin('CSCI 220', 700, 700)
# middle = graphics.Point(350,350)
# middle.draw(window)
# input()
from graphics import Point, GraphWin, Circle
win = GraphWin("Face", 700, 700)
face_center_point = Point(350,100)
face = Circle(face_center_point, 100)
face.draw(win)

left_eye = Circle(Point(325,60),20)
right_eye = Circle(Point(375,60),20)

left_eye.setFill('light blue')
left_eye.setOutline('green')

right_eye.setFill('light blue')
right_eye.setOutline('green')

left_eye.draw(win)
right_eye.draw(win)
input('hit enter to continue')

