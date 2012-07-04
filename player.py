from character import Character
from vector import Vec2

class Player:
    __acceleration = Vec2(0,0)
    __speed = Vec2(0,0)
    __position = Vec2(0,0)
    __isDamaged = 0
    
    def __init__(self):
        self.__speed.x = 1
        self.__speed.y = 0
    def setSpeed(self,speedX,speedY):
        self.__speed.x = speedX
        self.__speed.y = speedY
    def setSpeed(self,speed):
        self.__speed = speed
    def setSpeedX(self,speedX):
        self.__speed.x = speedX
    def setSpeedY(self,speedY):
        self.__speed.y = speedY
    def setPosition(self,position):
        self.__position = position
    def update(self):
        self.__speed.x += self.__acceleration.x
        self.__speed.y += self.__acceleration.y
        self.__position.x += self.__speed.x
        self.__position.y += self.__speed.y
