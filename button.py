from vector import Vec2
import math

class Shape:
    def __init__(self):
        None
    def isInner(self):
        None
    
    
class CircleShape(Shape):
    radius = 0

    def __init__(self,radius):
        Shape.__init__(self)
        self.radius = radius

    def isInner(self,position,coord):
        if(math.sqrt(math.pow(position.x - coord.x,2) + math.pow(position.y - coord.y,2)) <= self.radius):
            return True

        return False

class RectShape(Shape):
    width = 0
    height = 0

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def isInner(self,position,coord):
        if(position.x - self.width/2 <= coord.x and coord.x <= position.x + self.width/2):
            if(position.y - self.height/2 <= coord.y and coord.y <= position.y + self.height/2):
                return True

        return False

class Button:
    shape = None
    position = Vec2(0,0)

    def __init__(self,x,y,radius):
        self.position.x = x
        self.position.y = y
        shape = CircleShape(radius)

    def __init__(self,position):
        if(isinstance(position,Vec2)):
           self.position = position
        else:
           self.position.x = position[0]
           self.position.y = position[1]
    def isInner(self,coord):
        return shape.isClicked(position,coord)
