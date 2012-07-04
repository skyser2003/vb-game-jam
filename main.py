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
SCENE_MAIN_MENU = 0
SCENE_GAME = 1
SCENE_DEATH = 2
SCENE_INSTRUCTION = 3
SCENE_ESC = 4

def createLoveQuestion(LoverFileName,LoveeFileName,OX):
    return LoveQuestion(charDir + LoverFileName,charDir + LoveeFileName,OX)

def main():
    #Initialize
    pygame.init()
    screen = pygame.display.set_mode((700,450))
    pygame.display.set_caption("Dinosaur Run")
    background = pygame.image.load("images/background.png")
    redColor = pygame.Color(255,0,0)

    #Load images and colors
    start = pygame.image.load("images/start.png") 
    background = pygame.image.load("images/background.png")
    sky = pygame.image.load("images/sky.png")
    cloud = pygame.image.load("images/cloud.png")
    heart1 = pygame.image.load("images/heart.png")
    heart2 = pygame.image.load("images/heart2.png")
    stone = pygame.image.load("images/stone.png")
    black = pygame.Color(0,0,0)
    
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
    deathCharacter = pygame.image.load("images/bite.png")

    #Initial usic file import
    startmenu_bgm = pygame.mixer.Sound("sounds/startmenu.wav")
    play_bgm = pygame.mixer.Sound("sounds/play.wav")
    gameover_bgm = pygame.mixer.Sound("sounds/gameover.wav")

    #Create clock
    clock = pygame.time.Clock()
    running = True
    state = SCENE_MAIN_MENU

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

    questionsLoverImage = ()
    questionsLoveeImage = ()

    loverPosition = (191,72)
    loveePosition = (354,72)
    heartPosition = (310,119)

    #Load questions image
    for i in range(0,len(questions)):
        questionsLoverImage = questionsLoverImage[:i] + (pygame.image.load(questions[i].LoverDir),)
        questionsLoveeImage = questionsLoveeImage[:i] + (pygame.image.load(questions[i].LoveeDir),)

    #True False buttons
    trueButtonPosition = (484,84)
    falseButtonPosition = (484,121)

    trueImage = pygame.image.load("images/v.png")
    falseImage = pygame.image.load("images/x.png")

    trueFalseButtonSize = (trueImage.get_width(),trueImage.get_height())
    
    trueButton = Button(Vec2(trueButtonPosition[0] + trueFalseButtonSize[0]/2,trueButtonPosition[1] + trueFalseButtonSize[1]/2))
    falseButton = Button(Vec2(falseButtonPosition[0] + trueFalseButtonSize[0]/2,falseButtonPosition[1] + trueFalseButtonSize[1]/2))

    trueButton.setShape(RectShape(trueFalseButtonSize[0],trueFalseButtonSize[1]))
    falseButton.setShape(RectShape(trueFalseButtonSize[0],trueFalseButtonSize[1]))

    #Life points and stone
    life1Position = (28,37)
    life2Position = (68,37)
    life3Position = (108,37)
    stonePosition = (7,0)

    #Game numerics
    timer = 0
    rotateTimer = 0
    playerx = 300
    addx = 1
    dinox = 15
    addPlayerx = 1
    addDinox = 1
    life = 3
    deathAnimationCounter = 0
    fps = 100
    bgm = False
    deathCharacterPosition = (250,310)


    while running:
        screen.blit(sky, (0,0))
        
        #Main Menu
        if state == SCENE_MAIN_MENU:
            if bgm == False:
                startmenu_bgm.play()
                bgm = True
            
            screen.blit(start,(0,0))
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

                    if button1.isInner(coord) == True:
                        state = SCENE_GAME
                        startmenu_bgm.stop()
                        bgm = False

                    if button2.isInner(coord) == True:
                        state = SCENE_INSTRUCTION
                    if button3.isInner(coord) == True:
                        startmenu_bgm.stop()
                        bgm = False
                        running = False

                #Game playing 
                if event.type == KEYDOWN:
                    state = SCENE_GAME

        #In-game
        elif state == SCENE_GAME:
            if bgm == False:
                play_bgm.play()
                bgm = True

            #rolling background
            screen.blit(background,(rotateTimer,0))
            screen.blit(background,(rotateTimer+700,0))
            rotateTimer -= 1

            #Life points and stone
            screen.blit(stone,stonePosition)
            if(1 <= life):           
                screen.blit(heart1,life1Position)
            if(2 <= life):
                screen.blit(heart1,life2Position)
            if(3 <= life):
                screen.blit(heart1,life3Position)

            
            #player animation 
            if rotateTimer == -700:
                rotateTimer = 0
                
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

            #If 120 frame has passed with question on, show question
            if(questionOffTimer == 120):
                questionOffTimer = 0
                questionOn = True
                questionCurrentNo = random.randrange(0,len(questions))

            #If 120 frame has passed with question on, remove question and decrease life
            if(questionOnTimer == 120):
                questionOnTimer = 0
                questionOn = False
                questionCurrentNo = -1
                life -= 1
                
            #Question is on.  Show question
            if(questionOn == True):
                #Draw cloud
                #screen.blit(cloud,(0,0))
                #Why slow???

                #Draw characters
                screen.blit(questionsLoverImage[questionCurrentNo],loverPosition)
                screen.blit(questionsLoveeImage[questionCurrentNo],loveePosition)
                #Draw heart
                screen.blit(heart2,heartPosition)
                #Draw buttons
                screen.blit(trueImage,trueButtonPosition)
                screen.blit(falseImage,falseButtonPosition)
                
            for event in pygame.event.get():
                #Quit game
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    state = SCENE_ESC
                    play_bgm.stop()
                    bgm = False

                #Mouse clicked, check whether trueButton or falseButton is clicked
                elif event.type == MOUSEBUTTONDOWN:
                    mousex,mousey = event.pos
                    coord = Vec2(mousex,mousey)

                    #True button clicked
                    if(trueButton.isInner(coord) == True):
                        if(questionOn == True):
                            if(questions[questionCurrentNo].answer == True):
                                questionOn = False
                                questionOnTimer = 0
                            #Wrong
                            else:
                                life -= 1

                    #False button clicked
                    if(falseButton.isInner(coord) == True):
                        if(questionOn == True):
                            #Wrong
                            if(questions[questionCurrentNo].answer == True):
                                life -= 1
                            else:
                                questionOn = False
                                questionOnTimer = 0

                    if event.type == QUIT:
                        running = False
                    elif event.type == KEYDOWN:
                        state = SCENE_ESC
                        play_bgm.stop()
                        bgm = False
                        running = False
                    elif event.type == MOUSEBUTTONUP:
                        mousex, mousey = event.pos

            #Dead
            if(life == 0):
                state = SCENE_DEATH

        #Instruction page
        elif state == SCENE_INSTRUCTION:
            pygame.draw.rect(screen,black, (0,0,700,450))
            screen.blit(home_button, (520,320))
            button4 = Button(Vec2(600,350))
            button4.setShape(RectShape(160,60))
            
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    coord = Vec2(mousex,mousey)

                    if button4.isInner(coord) == True:
                        state = SCENE_MAIN_MENU

        #Dead.  Show death animation
        elif state == SCENE_DEATH:
            screen.blit(background,(0,0))
            screen.blit(deathCharacter,deathCharacterPosition)

            deathAnimationCounter += 1

            if(deathAnimationCounter == fps):
                running = False
            
            play_bgm.stop()
            gameover_bgm.play()
            bgm = True

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
                        state = SCENE_MAIN_MENU
                        gameover_bgm.stop()
                        bgm = False

        clock.tick(fps)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
        main()
