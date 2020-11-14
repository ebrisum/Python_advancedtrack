from week_8.geometry.Point import Point

"""
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result
"""

def distance(point1, point2):
    delta_x = point1.x - point2.x
    delta_y = point1.y - point2.y
    distance = (delta_x ** 2 + delta_y ** 2) ** .5
    return distance

print(Point(-4,10).slope_from_origin)

