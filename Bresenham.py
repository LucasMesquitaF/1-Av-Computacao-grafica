from typing import final
import Printer

class Bresenham():

    def __init__(self, initial_point, final_point):
        self.x1 = initial_point[0]
        self.x2 = final_point[0]
        self.y1 = initial_point[1]
        self.y2 = final_point[1]
        self.m = (initial_point[1] - final_point[1]) / (initial_point[0] - final_point[0])

    def Bresenham(self):
        points = []
        swipe_coordinates, swipe_x, swipe_y = Bresenham.reflection(self)
        e = self.m - 0.5
        print(self.x2)
        points.append([self.x1,self.y1])
        #Printer.DesenharPixel(x,y)
        while self.x1 < self.x2:
            if e > 0:
                self.y1 += 1
                e -= 1
            self.x1 += 1
            print(e)
            e += self.m
            points.append([self.x1,self.y1])
            #Printer.DesenharPixel(x,y)
        Bresenham.reflectionInverse(self, swipe_coordinates, swipe_x, swipe_y, points)
        print(points)
        return points
        
    def reflection(self):
        swipe_coordinates, swipe_x, swipe_y = 0,0,0
        x1, y1 = self.x1,self.y1
        x2, y2 = self.x2, self.y2
        if self.m > 1 or self.m < -1:
            self.x1,self.y1= y1,x1
            self.x2, self.y2 = y2, x2
            swipe_coordinates = True
        if x1 > x2:
            self.x1 = -x1
            self.x2 = -x2
            swipe_x = True
        if y1 > y2:
            self.y1 = -y1
            self.y2 = -y2
            swipe_y = True
        return swipe_coordinates, swipe_x, swipe_y

    def reflectionInverse(self, swipe_coordinates, swipe_x,swipe_y, points):
        if swipe_coordinates:
            for point in points:
                point[0],point[1] = point[1], point[0]
        if swipe_x:
            for point in points:
                point[0] *= -1
        if swipe_y:
            for point in points:
                point[1] *= -1
        
B = Bresenham((0,3),(3,9))
points = B.Bresenham()

for point in points:
    Printer.DesenharPixel(point[0], point[1])