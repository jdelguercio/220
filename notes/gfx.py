import graphics

my_point = graphics.Point(50,70)
point_a = graphics.Point(70,90)
point_a.move(10,0)

window = graphics.GraphWin('CSCI 220', 700, 700)
middle = graphics.Point(350,350)
middle.draw(window)
input()
