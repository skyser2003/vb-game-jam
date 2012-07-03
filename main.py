import os, pygame
from util import *
from pygame.locals import *
from pygame.compat import geterror

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,450))
    pygame.display.set_caption("Dinosaur Run")

    background = pygame.image.load("images/background.png")
    redColor = pygame.Color(255,0,0)
    #screen.blit(background, (0,0))
    

    clock = pygame.time.Clock()

    running = True
    state = 0

    font = pygame.font.Font(None, 18)
    largeFont = pygame.font.Font(None, 30)
    
    
    while running:
        

        if state == 0:
            pygame.draw.circle(background, redColor, (300,300),20)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    state = 1
                    
        
        elif state == 1:
            screen.blit(background, (0,0))
            for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    elif event.type == KEYDOWN:
                        running = False
                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos
                        print (mousex,mousey)

        
            
        pygame.display.update()
    
    pygame.quit()

if __name__ == '__main__':
        main()
