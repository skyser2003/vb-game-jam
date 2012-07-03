import os, pygame
from util import *
from vector import Vec2
from button import Button
from button import RectShape
from pygame.locals import *
from pygame.compat import geterror

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,450))
    pygame.display.set_caption("Dinosaur Run")
    
    background = pygame.image.load("images/background.png")
    sky = pygame.image.load("images/sky.png")
    red = pygame.Color(255,0,0)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0,0,255)
    white = pygame.Color(255,255,255)
    black = pygame.Color(0,0,0)
    

    clock = pygame.time.Clock()

    running = True
    state = 0

    font = pygame.font.Font(None, 18)
    largeFont = pygame.font.Font(None, 30)
    
    
    while running:
        

        if state == 0:
            screen.blit(pygame.image.load("images/start.png"),(0,0))
            pygame.draw.rect(screen, red,(270,110,160,100))
            pygame.draw.rect(screen, green, (270,220,160,100))
            pygame.draw.rect(screen, blue, (270,330,160,100))
            button1 = Button(Vec2(350,160))
            button1.setShape(RectShape(160,100))
            button2 = Button(Vec2(350,270))
            button2.setShape(RectShape(160,100))
            button3 = Button(Vec2(350,380))
            button3.setShape(RectShape(160,100))

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    coord = Vec2(mousex,mousey)
                    print (mousex,mousey)
                    if button1.isInner(coord) == True:
                        state = 1
                    if button2.isInner(coord) == True:
                        state = 2
                    if button3.isInner(coord) == True:
                        running = False                              
        
        elif state == 1:
            screen.blit(sky, (0,0))
            screen.blit(background, (0,0))
            for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    elif event.type == KEYDOWN:
                        state = 3
                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        print (mousex,mousey)
                        
        elif state == 2:
            pygame.draw.rect(screen,black, (0,0,700,450))
            pygame.draw.rect(screen,white,(520,320,160,60))
            button4 = Button(Vec2(600,350))
            button4.setShape(RectShape(160,60))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    coord = Vec2(mousex,mousey)
                    print (mousex,mousey)
                    if button4.isInner(coord) == True:
                        state = 0
                    
        elif state == 3:
            pygame.draw.rect(screen,black,(0,0,700,450))
            pygame.draw.rect(screen,white,(520,320,160,60))
            pygame.draw.rect(screen,white,(20,320,160,60))
            button5 = Button(Vec2(600,350))
            button5.setShape(RectShape(160,60))
            button6 = Button(Vec2(100,350))
            button6.setShape(RectShape(160,60))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    coord = Vec2(mousex,mousey)
                    print (mousex,mousey)
                    if button5.isInner(coord) == True:
                        running = False
                    if button6.isInner(coord) == True:
                        state = 0
        
            
        pygame.display.update()
    
    pygame.quit()

if __name__ == '__main__':
        main()
