from week_8.geometry.Point import Point

point_p = Point(10, 6)


def distance(point1, point2):
    delta_x = point1.x - point2.x
    delta_y = point1.y - point2.y
    distance = (delta_x ** 2 + delta_y ** 2) ** .5
    return distance

print(Point(0,0).midpoint_line(3,3))

