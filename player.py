from vector import Vec2
import spritesheet
from spritesheet import SpriteStripAnim

class player:
    #__acceleration = Vec2(0,0)
    #__speed = Vec2(0,0)
    #__position = Vec2(0,0)
    __isDamaged = 0
    __size = 100
    __sprite = None
    def __init__(self):
        #self.__speed.x = 1
        #self.__speed.y = 0
        if player.__sprite is None:
            player.__sprite = spritesheet.spritesheet("images/player.png")
        self.image = player.__sprite.image_at((player.__size,0,player.__size,player.__size), -1)
        

    def update(self):
        player.__sprite.SpriteStripAnim.iter()
        image = player.__sprite.next()
        pygame.display.update()
        
    
    """def setSpeed(self,speedX,speedY):
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
    """

    
