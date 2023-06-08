import pygame
import random
from sys import exit
import a
import time

pygame.init()

screen=pygame.display.set_mode((1152,570))
pygame.display.set_caption('Cricket')
clock=pygame.time.Clock()
bg=pygame.image.load('11u.png')
font=pygame.font.Font('f1.ttf',40)
midgamefont=pygame.font.Font('f1.ttf',40)
wk=pygame.image.load('w1.png')
s=pygame.image.load('scorebg4.png')
ball=pygame.image.load('ball1.png')
ab=pygame.image.load('intro1.png')
ibg=pygame.image.load('ibg.png')
bowlingmachine=pygame.image.load('bowler.png')
out=pygame.image.load('out.png')
six=pygame.image.load('6.png')
four=pygame.image.load('4.png')
sixump=pygame.image.load('sixump.png')
outump=pygame.image.load('outump.png')
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
fourump=[fourump1,fourump2,fourump3,fourump4,fourump5,fourump6,fourump7,fourump8,fourump9,fourump10]
findex=0
title=font.render('Cricbat.play',True,(0,100,100))
q=font.render('Choose the difficulty level',True,(0,200,150))
q2=font.render('Choose no of overs',True,(0,150,200))
o11=font.render('Easy',True,(255,165,0))
o12=font.render('Medium',True,(255,165,0))
o13=font.render('Hard',True,(255,165,0))
o21=font.render('2',True,(255,165,0))
o22=font.render('5',True,(255,165,0))
o23=font.render('10',True,(255,165,0))
fr=pygame.image.load('optionbg.png')
bfr1=pygame.image.load('fr1.png')
bfr2=pygame.image.load('fr2.png')
bfr3=pygame.image.load('fr3.png')
bfr4=pygame.image.load('fr4.png')
bfr5=pygame.image.load('fr5.png')
bfg1=pygame.image.load('fg1.png')
bfg2=pygame.image.load('fg2.png')
bfg3=pygame.image.load('fg3.png')
bfg4=pygame.image.load('fg4.png')
bfg5=pygame.image.load('fg5.png')
bindex=0
listb=[bfr1,bfr2,bfr3,bfr4,bfr5]
listb2=[bfg1,bfg2,bfg3,bfg4,bfg5]

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


def createbackground():
    screen.blit(bg,(0,0))
    screen.blit(wk,(560,115))
    screen.blit(s,(0,520))
    screen.blit(bowlingmachine,(455,330))
    show_score(score,wicket,target,balls)

def bowl():
    
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
    

    
    

def midgame_screen():
    global findex
    a1=midgamefont.render('Press spacebar to continue',True,(64,169,196))
    a2=midgamefont.render('Last ball score='+str(currentscore),True,(255,255,255))
    # a3=midgamefont.render('Out',True,'Red')
    
    if currentwicket==1:
        screen.blit(outump,(0,0))
        screen.blit(out,(75,270))
        screen.blit(a1,(320,210))
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
    else:
        screen.blit(fourump[0],(0,0))
        screen.blit(a1,(320,210))
        screen.blit(a2,(350,250))





def show_score(a,b,target,balls_left):
    tscore=font.render('Score='+str(a)+'/'+str(b),True,'Blue')
    t=font.render('Target='+str(target),True,(51,255,255))
    b=font.render('Balls left='+str(balls_left),True,'Red')
    screen.blit(t,(400,530))
    screen.blit(b,(900,530))
    screen.blit(tscore,(10,530))
    
def shot(x):
    global bx,by
    global sindex,bindex
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

