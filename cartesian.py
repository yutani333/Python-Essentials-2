import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return str(math.hypot((self.__x - x),(self.__y - y)))

    def distance_from_point(self, point):
        return math.hypot((self.__x - point.getx()), (self.__y - point.gety()))

class Triangle:
    def __init__(self, vert1, vert2, vert3):
        self.__verts = [vert1, vert2, vert3]

    def perimeter(self):
        points = len(self.__verts)
        perimeter = 0
        perimeter += self.__verts[0].distance_from_point(self.__verts[points-1])
        for v in range(1, points):
            perimeter += self.__verts[v].distance_from_point(self.__verts[v-1])
        return perimeter

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
