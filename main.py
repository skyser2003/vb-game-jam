import os, pygame
from util import *
from pygame.locals import *
from pygame.compat import geterror

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,450))
    pygame.display.set_caption("Dinosaur Run")
    #pygame.mouse.set_visible(0)

    background = pygame.image.load("images/background.png")
    redColor = pygame.Color(255,0,0)
    screen.blit(background, (0,0))
    pygame.draw.circle(background, redColor, (300,300),20)

    clock = pygame.time.Clock()

    running = True
    state = 0

    font = pygame.font.Font(None, 18)
    largeFont = pygame.font.Font(None, 30)
    
    pygame.display.update()
    while running:
        pygame.draw.line(background, redColor, (0,0),(700,350),5)

    
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
            

    
    pygame.quit()

if __name__ == '__main__':
        main()
