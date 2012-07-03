import os, pygame
from util import *
from pygame.locals import *
from pygame.compat import geterror

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,450))
    pygame.display.set_caption("Dinosaur Run")
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()
    counter = 0

    background = pygame.image.load("/Users/FrozenGuy/Pictures/Raichu.png")

    while True:
        screen.blit(background,(0,0))
        clock.tick(60)
        pygame.display.update()
        counter += 1

        if(counter == 300):
            break
        
    pygame.quit()

if __name__ == '__main__':
        main()
