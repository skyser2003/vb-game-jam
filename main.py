import os, pygame
from util import *
from vector import Vec2
from button import Button
from button import RectShape
from question import LoveQuestion
import spritesheet
import player
from spritesheet import SpriteStripAnim
from pygame.locals import *
from pygame.compat import geterror
import random

charDir = "images/character/"

def createLoveQuestion(LoverFileName,LoveeFileName,OX):
    return LoveQuestion(charDir + LoverFileName,charDir + LoveeFileName,OX)

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,450))
    pygame.display.set_caption("Dinosaur Run")

    black = pygame.Color(0,0,0)
        
    #Background images    
    background = pygame.image.load("images/background.png")
    sky = pygame.image.load("images/sky.png")
    cloud = pygame.image.load("images/cloud.png")
    #Button images
    start_button = pygame.image.load("images/start_button.png")
    instruction_button = pygame.image.load("images/instruction_button.png")
    end_button1 = pygame.image.load("images/end_button1.png")
    home_button = pygame.image.load("images/home_button.png")
    end_button2 = pygame.image.load("images/end_button2.png")
    #Character images
    player1 = pygame.image.load("images/player1.png")
    player2 = pygame.image.load("images/player2.png")
    player3 = pygame.image.load("images/player3.png")
    player4 = pygame.image.load("images/player4.png")
    dino1 = pygame.image.load("images/dino1.png")
    dino2 = pygame.image.load("images/dino2.png")
    dino3 = pygame.image.load("images/dino3.png")
    dino4 = pygame.image.load("images/dino4.png")

    #Initial usic file import
    startmenu_bgm = pygame.mixer.Sound("sounds/startmenu.wav")
    play_bgm = pygame.mixer.Sound("sounds/play.wav")
    gameover_bgm = pygame.mixer.Sound("sounds/gameover.wav")

    #Create clock
    clock = pygame.time.Clock()

    running = True
    state = 0

    #Fonts
    font = pygame.font.Font(None, 18)
    largeFont = pygame.font.Font(None, 30)

    #Questions
    questions = []
    questions.insert(0,createLoveQuestion("cat.png","mouse.png",True))
    questions.insert(0,createLoveQuestion("monkey.png","banana.png",True))
    questions.insert(0,createLoveQuestion("samsung.png","mac.png",False))
    
    questionOffTimer = 0
    questionOnTimer = 0
    
    questionOn = False
    questionCurrentNo = -1

    trueButton = Button(Vec2(460,60))
    falseButton = Button(Vec2(460,260))

    trueButton.setShape(RectShape(120,120))
    falseButton.setShape(RectShape(120,120))
    
    timer = 0
    rotateTimer = 0
    playerx = 300
    dinox = 15
    addPlayerx = 1
    addDinox = 1
    bgm = False
    #pygame.mixer.Channel.play(startmenu_bgm, -1)
    while running:
        screen.blit(sky, (0,0))
        
        #Main Menu
        if state == 0:
            if bgm == False:
                startmenu_bgm.play()
                bgm = True            
            screen.blit(pygame.image.load("images/start.png"),(0,0))
            screen.blit(start_button, (270,110))
            screen.blit(instruction_button, (270,220))
            screen.blit(end_button1, (270,330))
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
                        startmenu_bgm.stop()
                        bgm = False
                        state = 1
                    if button2.isInner(coord) == True:
                        state = 2
                    if button3.isInner(coord) == True:
                        startmenu_bgm.stop()
                        bgm = False
                        running = False
            

        elif state == 1:
            if bgm == False:
                play_bgm.play()
                bgm = True
            #rolling background
            screen.blit(background,(rotateTimer,0))
            screen.blit(background,(rotateTimer+700,0))
            rotateTimer -= 1
            if rotateTimer == -700:
                rotateTimer =0
            #player+dino animation        
            if timer%15 == 0:
                screen.blit(player1, (playerx,260))
                screen.blit(dino1, (dinox,300))
            elif timer%15 == 1:
                screen.blit(player1, (playerx,260))
                screen.blit(dino1, (dinox,300))
            elif timer%15 == 2:
                screen.blit(player2, (playerx,260))
                screen.blit(dino2, (dinox,300))
            elif timer%15 == 3:
                screen.blit(player2, (playerx,260))
                screen.blit(dino2, (dinox,300))
            elif timer%15 == 4:
                screen.blit(player3, (playerx,260))
                screen.blit(dino3, (dinox,300))
            elif timer%15 == 5:
                screen.blit(player3, (playerx,260))
                screen.blit(dino3, (dinox,300))
            elif timer%15 == 6:
                screen.blit(player3, (playerx,260))
                screen.blit(dino3, (dinox,300))
            elif timer%15 == 7:
                screen.blit(player4, (playerx,260))
                screen.blit(dino4, (dinox,300))
            elif timer%15 == 8:
                screen.blit(player4, (playerx,260))
                screen.blit(dino4, (dinox,300))
            elif timer%15 == 9:
                screen.blit(player4, (playerx,260))
                screen.blit(dino4, (dinox,300))
            elif timer%15 == 10:
                screen.blit(player3, (playerx,260))
                screen.blit(dino3, (dinox,300))
            elif timer%15 == 11:
                screen.blit(player3, (playerx,260))
                screen.blit(dino3, (dinox,300))
            elif timer%15 == 12:
                screen.blit(player2, (playerx,260))
                screen.blit(dino3, (dinox,300))
            elif timer%15 == 13:
                screen.blit(player2, (playerx,260))
                screen.blit(dino2, (dinox,300))
            elif timer%15 == 14:
                screen.blit(player1, (playerx,260))
                screen.blit(dino1, (dinox,300))
            #moving player back and forth
            if playerx == 280:
                addPlayerx = 1
            if playerx == 320:
                addPlayerx = -1
            #moving dino back and forth
            if dinox == 10:
                addDinox = 1
            if dinox == 40:
                addDinox = -1
                
            playerx += addPlayerx
            dinox += addDinox
            timer += 1

            screen.blit(cloud, (0,0))

            #questions


            if(questionOn == False):
                questionOffTimer += 1
            else:
                questionOnTimer += 1

            if(questionOffTimer == 120):
                questionOffTimer = 0
                questionOn = True
                questionCurrentNo = random.randrange(0,len(questions))
                print questions[questionCurrentNo].answer

            if(questionOnTimer == 60):
                questionOnTimer = 0
                questionOn = False
                questionCurrentNo = -1
                
            #Show question
            if(questionOn == True):
                #Characters
                screen.blit(pygame.image.load(questions[questionCurrentNo].LoverDir),(0,0))
                screen.blit(pygame.image.load(questions[questionCurrentNo].LoveeDir),(200,0))
                #Buttons
                screen.blit(pygame.image.load(questions[questionCurrentNo].LoverDir),(400,0))
                screen.blit(pygame.image.load(questions[questionCurrentNo].LoveeDir),(400,200))
          
    
            for event in pygame.event.get():
                #GO TO GAMEOVER STATE
                if event.type == KEYDOWN:
                    play_bgm.stop()
                    bgm = False
                    state = 3
                    
                #For Debugging, print mouse position
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos


                #Mouse clicked, check whether trueButton or falseButton is clicked
                elif event.type == MOUSEBUTTONDOWN:
                    mousex,mousey = event.pos
                    coord = Vec2(mousex,mousey)

                    if(trueButton.isInner(coord)):
                        print "True clicked"

                        if(questionOn == True):
                            if(questions[questionCurrentNo].answer == True):
                                print "Answer Correct!"
                            else:
                                print "Answer Wrong!"

                    if(falseButton.isInner(coord)):
                        print "False Clicked"

                        if(questionOn == True):
                            if(questions[questionCurrentNo].answer == True):
                                print "Answer Wrong"
                            else:
                                print "Answer Correct!"

                    if event.type == QUIT:
                        running = False
                    elif event.type == KEYDOWN:
                        play_bgm.stop()
                        bgm = False
                        state = 3
                        running = False
                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos

        
        #Instruction page
        elif state == 2:
            pygame.draw.rect(screen,black, (0,0,700,450))
            screen.blit(home_button, (520,320))
            button4 = Button(Vec2(600,350))
            button4.setShape(RectShape(160,60))
            
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    coord = Vec2(mousex,mousey)

                    if button4.isInner(coord) == True:
                        state = 0
            
        #In-game menu(esc pressed)
        elif state == 3:
            if bgm == False:
                gameover_bgm.play()
                bgm = True
            pygame.draw.rect(screen,black,(0,0,700,450))
            screen.blit(home_button, (20,320))
            screen.blit(end_button2, (520,320))
            button5 = Button(Vec2(600,350))
            button5.setShape(RectShape(160,60))
            button6 = Button(Vec2(100,350))
            button6.setShape(RectShape(160,60))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    coord = Vec2(mousex,mousey)

                    if button5.isInner(coord) == True:
                        running = False
                    if button6.isInner(coord) == True:
                        gameover_bgm.stop()
                        bgm = False
                        state = 0
                        
        
        clock.tick(100)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
        main()
