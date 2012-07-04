from character import Character
from vector import Vec2
import spritesheet
from spritesheet import SpriteStripAnim

class Player(Character):
    __damageReduceSpeed = 10
    __isDamaged = False
    __damageProgressTime = 0

    def getAttacked(self):
        self.__speed.x -= self.__damageReduceSpeed
        self.__isDamaged = True
        self.__damageProgressTime = 0
    def recoverFromAttack(self):
        self.__speed.x += self.__damageReduceSpeed
        self.__isDamaged = False
        self.__damageProgressTime = 0
    def update(self,fps):
        Character.update(self,fps)
        
        if(self.__isDamaged == True):
            self.__damageProgressTime += 60/fps
