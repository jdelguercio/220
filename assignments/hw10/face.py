from graphics import *


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        self.mouth.undraw()
        smile_bottom_point = self.mouth.getP1()
        smile_y = smile_bottom_point.getY()
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        smile_x = abs(p1.getX() - p2.getx())
        self.smiley = Polygon(p1, p2, Point(smile_x, smile_y))
        self.smiley.draw(self.window)




    def shock(self):
        self.mouth.undraw()
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        smile_x = abs(p1.getX() - p2.getx())
        radius = self.left_eye.getRadius()
        self.new_mouf = Circle(smile_x, radius)
        self.new_mouf.draw(self.window)




    def wink(self):
        self.mouth.undraw()
        smile_bottom_point = self.mouth.getP1()
        smile_y = smile_bottom_point.getY()
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        smile_x = abs(p1.getX() - p2.getx())
        self.smiley = Polygon(p1, p2, Point(smile_x, smile_y))
        self.smiley.draw(self.window)
        self.left_eye.undraw()

