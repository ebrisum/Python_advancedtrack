class Point:
    """
    Point class represents and manipulates x and y coordinates
    """
    def __init__(self, x=0, y=0):
        """"Create a new point at the origin"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def distance_from_origin(self):
        return (self.x * self.x + self.y * self.y) ** .5

    def reflect_x(self):
        return "{}, {}".format(self.x, self.y * -1)

    def slope_from_origin(self):
        return (self.y/self.x)
        # What cases will cause this method to fail????
        # when self.x = 0

    def get_line_to(self, x, y):
        dif_y = self.y - y
        dif_x = self.x - x
        slope = int(dif_y / dif_x)
        b = int(y - (slope * x))
        return slope
        #when will this method fail? prob. when dif_x = 0

    def midpoint_line(self, point1, point2, point3):
        midpointAB = [(point1.x + point2.x)/2, (point1.y + point2.y)/2]
        midpointAC = [(point1.x + point3.x)/2, (point1.y + point3.y)/2]
        slope_AB = point1.get_line_to(point2.x, point2.y)
        slope_AC = point1.get_line_to(point3.x, point3.y)
        perp_gradientAB = ((slope_AB) ** -1) * -1
        perp_gradientAC = ((slope_AC) ** -1) * -1
        equation_perp_bisectorAB = slope_AB*(midpointAB[1])


