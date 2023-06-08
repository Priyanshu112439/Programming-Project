import pygame
import random
from sys import exit
import a
import time

#initiating pygame
pygame.init()
#Creating display
screen=pygame.display.set_mode((1152,570))
#Naming 
pygame.display.set_caption('Cricket')
clock=pygame.time.Clock()

#game background image
bg=pygame.image.load('11u.png')

#font style
font=pygame.font.Font('f1.ttf',40)
midgamefont=pygame.font.Font('f1.ttf',40)

#wicket image
wk=pygame.image.load('w1.png')
#scoreboard background
s=pygame.image.load('scorebg4.png')

#ball image
ball=pygame.image.load('ball1.png')

#start screen background
ab=pygame.image.load('intro1.png')
ibg=pygame.image.load('ibg.png')

#bowling machine image
bowlingmachine=pygame.image.load('bowler.png')
#images to show during respective events
out=pygame.image.load('out.png')
six=pygame.image.load('6.png')
four=pygame.image.load('4.png')
#umpire signals
sixump=pygame.image.load('sixump.png')
outump=pygame.image.load('outump.png')
#umpire animation frames for four
fourump1=pygame.image.load('fourump1.png')
fourump2=pygame.image.load('fourump2.png')
fourump3=pygame.image.load('fourump3.png')
fourump4=pygame.image.load('fourump4.png')
fourump5=pygame.image.load('fourump5.png')
fourump6=pygame.image.load('fourump6.png')
fourump7=pygame.image.load('fourump7.png')
fourump8=pygame.image.load('fourump8.png')
fourump9=pygame.image.load('fourump9.png')
fourump10=pygame.image.load('fourump10.png')
#list of the frames
fourump=[fourump1,fourump2,fourump3,fourump4,fourump5,fourump6,fourump7,fourump8,fourump9,fourump10]
#index of umpire animation
findex=0

#game title for start screen
title=font.render('Cricbat.play',True,(0,100,100))
# Strings of the difficulty and ivers
q=font.render('Choose the difficulty level',True,(0,200,150))
q2=font.render('Choose no of overs',True,(0,150,200))
o11=font.render('Easy',True,(255,165,0))
o12=font.render('Medium',True,(255,165,0))
o13=font.render('Hard',True,(255,165,0))
o21=font.render('2',True,(255,165,0))
o22=font.render('5',True,(255,165,0))
o23=font.render('10',True,(255,165,0))

# background of the options
fr=pygame.image.load('optionbg.png')

#frames of shot 1
bfr1=pygame.image.load('fr1.png')
bfr2=pygame.image.load('fr2.png')
bfr3=pygame.image.load('fr3.png')
bfr4=pygame.image.load('fr4.png')
bfr5=pygame.image.load('fr5.png')

#frames of shot2
bfg1=pygame.image.load('fg1.png')
bfg2=pygame.image.load('fg2.png')
bfg3=pygame.image.load('fg3.png')
bfg4=pygame.image.load('fg4.png')
bfg5=pygame.image.load('fg5.png')
#index of shot list
bindex=0

#list of shots
listb=[bfr1,bfr2,bfr3,bfr4,bfr5]
listb2=[bfg1,bfg2,bfg3,bfg4,bfg5]

#setting the initial values of variables
bx=560
by=560
index=0
sindex=0
currentscore=0
currentwicket=0
randomball=random.randint(0,4)
score=0
wicket=0
active=5
wickett=10
overs=0
balls=0

#creating game background
def createbackground():
    screen.blit(bg,(0,0))
    screen.blit(wk,(560,115))
    screen.blit(s,(0,520))
    screen.blit(bowlingmachine,(455,330))
    show_score(score,wicket,target,balls)


# function to bowl the ball
def bowl():
    # calling the list containing the coordinates of different balls
    bl1=a.l1[randomball]
    global ballno,bx,by
    global index
    ballno=1
    if index<len(bl1)-2:
        index+=0.6
    else:
        index=len(bl1)-1
        
    bx=bl1[int(index)][0]
    by=bl1[int(index)][1]
    

    
    
# screen that appears after each ball is bowled
def midgame_screen():
    global findex
    a1=midgamefont.render('Press spacebar to continue',True,(64,169,196))
    a2=midgamefont.render('Last ball score='+str(currentscore),True,(255,255,255))
    # a3=midgamefont.render('Out',True,'Red')
    
    #if wicket falls
    if currentwicket==1:
        screen.blit(outump,(0,0))
        screen.blit(out,(75,270))
        screen.blit(a1,(320,210))

    #if batsman hits 6 or 4
    
    
    elif currentscore==6:
        screen.blit(sixump,(0,0))
        screen.blit(six,(75,270))
        screen.blit(a1,(320,210))
    elif currentscore==4:
        if findex<len(fourump)-1:
            findex+=0.15
        else:
            findex=0
        screen.blit(fourump[int(findex)],(0,0))
        screen.blit(four,(75,270))
        screen.blit(a1,(320,210))
    
    #in other cases
    else:
        screen.blit(fourump[0],(0,0))
        screen.blit(a1,(320,210))
        screen.blit(a2,(350,250))




#displaying score, target , wickets and balls left
def show_score(a,b,target,balls_left):
    tscore=font.render('Score='+str(a)+'/'+str(b),True,'Blue')
    t=font.render('Target='+str(target),True,(51,255,255))
    b=font.render('Balls left='+str(balls_left),True,'Red')
    screen.blit(t,(400,530))
    screen.blit(b,(900,530))
    screen.blit(tscore,(10,530))
    
#function of playing a shot    
def shot(x):
    global bx,by
    #shot index and ball index
    global sindex,bindex
 #callling the list of coordinates of ball after it is hit for a shot
    sl1=a.l2[x]
    if sindex<len(sl1)-1:
        sindex+=0.75
    else:
        sindex=len(sl1)-1
    bx=sl1[int(sindex)][0]
    by=sl1[int(sindex)][1]
    if bindex<len(listb)-1:
        bindex+=0.1
    else:
        bindex=len(listb)-1
    if x==0 or x==1 or x==2:
        screen.blit(listb2[int(bindex)],(530,75))
    else:
        screen.blit(listb[int(bindex)],(555,75))

