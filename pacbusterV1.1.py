#############################################################
#@Title : PacBuster                                         #
#@Author : Ugo Bourdon | Mathieu Noyelle                    #
#@Version : 1.1                                             #
#@Date : 6th June, 2017                                     #
#############################################################

from turtle import *
from random import *
import winsound

sc=getscreen()
##############################################################
#            initialise les paramètres de jeux               #  
##############################################################   
def debut():
    sc.reset()
    penup()
    
    sc.bgcolor("black")
    sc.register_shape("img/v0.gif")
    sc.register_shape("img/v1.gif")
    sc.register_shape("img/m1.gif")
    sc.register_shape("img/m2.gif")
    sc.register_shape("img/m3.gif")
    sc.register_shape("img/m4.gif")
    sc.register_shape("img/m5.gif")
    sc.register_shape("img/m6.gif")
    sc.register_shape("img/m7.gif")
    sc.register_shape("img/m8.gif")
    sc.register_shape("img/m9.gif")
    sc.register_shape("img/mi.gif")
    sc.register_shape("img/ma.gif")
    sc.register_shape("img/c1.gif")
    sc.register_shape("img/c2.gif")
    sc.register_shape("img/c3.gif")
    sc.register_shape("img/c4.gif")
    sc.register_shape("img/pacpac0.gif")
    sc.register_shape("img/pacpac90.gif")
    sc.register_shape("img/pacpac180.gif")
    sc.register_shape("img/pacpac270.gif")
    sc.register_shape("img/fantome_rouge.gif")
    sc.register_shape("img/fantome_rose.gif")
    sc.register_shape("img/fantome_bleu.gif")
    sc.register_shape("img/fantome_vert.gif")
    sc.register_shape("img/Pblanc.gif")
    sc.register_shape("img/ghostbuster.gif")
    sc.register_shape("img/vie.gif")

def menuCarte():
    debut()
    winsound.PlaySound('sounds/theme.wav',winsound.SND_ASYNC)
    penup()
    ht()  
    maison=Turtle()
    maison.shape("img/ghostbuster.gif")
    texte=Turtle()
    texte.ht()
    texte.penup()
    texte.pencolor("#FFF")
    texte.goto(-160,300)
    texte.write("PACBUSTER",font=("Arial",40,'normal'))
    texte.goto(-70,210)
    texte.write("m = monde 1",font=("Arial",15,'normal'))
    texte.goto(-70,180)
    texte.write("p = monde 2",font=("Arial",15,'normal'))
    animationMenuIntro()
    animationMenu()
    onkeypress(monde1,key="m")
    onkeypress(monde1,key="M")
    onkeypress(monde2,key="p")
    onkeypress(monde2,key="P")
    listen()
    
    
def menu():
    sc.reset()
    debut()
    penup()
    ht()  
    maison=Turtle()
    maison.shape("img/ghostbuster.gif")
    texte=Turtle()
    texte.ht()
    texte.penup()
    texte.pencolor("#FFF")
    texte.goto(-160,300)
    texte.write("PACBUSTER",font=("Arial",40,'normal'))
    texte.goto(-70,210)
    texte.write("F1 = lent",font=("Arial",15,'normal'))
    texte.goto(-70,180)
    texte.write("F2 = moyen",font=("Arial",15,'normal'))
    texte.goto(-70,150)
    texte.write("F3 = rapide",font=("Arial",15,'normal'))
    texte.goto(-70,120)
    texte.write("F4 = Xtrem",font=("Arial",15,'normal'))
    onkeypress(F1,key="F1")
    onkeypress(F2,key="F2")
    onkeypress(F3,key="F3")
    onkeypress(F4,key="F4")
    listen()

def monde1():#choix de la carte
    global niveau
    niveau="carte/carte.txt"
    sc.clear()
    menu()
def monde2():
    global niveau
    niveau="carte/carte(1).txt"
    sc.clear()
    menu()
    
def F1():
    global vitesseFANT,vitessePAC
    vitesseFANT=30
    vitessePAC=600
    parametreJeu()
    initJeu()

def F2():
    global vitesseFANT,vitessePAC
    vitesseFANT=30
    vitessePAC=450
    parametreJeu()
    initJeu()

def F3():
    global vitesseFANT,vitessePAC
    vitesseFANT=30
    vitessePAC=300
    parametreJeu()
    initJeu()

def F4():
    global vitesseFANT,vitessePAC
    vitesseFANT=30
    vitessePAC=150
    parametreJeu()
    initJeu()

def parametreJeu():
    global vitesse,cordpions,cordmurs,pions,murs,pas,PV
    cordpions=[]
    cordmurs=[]
    pions=[]
    murs=[]
    pas=30
    vitesse=0
    PV=3


def initJeu():
    global pacman,vitesse
    winsound.PlaySound('sounds/music.wav',winsound.SND_ASYNC)
    fondDeCarte()
    pointBlanc()
    pacman=Turtle()
    pacman.penup()
    pacman.goto(0,-150)
    afficherVieRest()
    fantome()
    Obstacle()
    pacman.shape("img/pacpac0.gif")
    maison=Turtle()
    maison.shape("img/ghostbuster.gif")
    vitesse=0
    anime()
    
def XYtoIJ(x,y):
    global i,j
    i=0
    j=0
    j=int((x+285)//30)
    i=int((y+315)//30)
    return i,j 

##############################################################
#            annimation du menu                              #  
##############################################################

def animationMenu():
    global pacmenu,ghostMenu1,ghostMenu2,ghostMenu3,ghostMenu4
    pacmenu.fd(30)
    ghostMenu1.fd(30)
    ghostMenu2.fd(30)
    ghostMenu3.fd(30)
    ghostMenu4.fd(30)
    sc.ontimer(animationMenu,400)

def animationMenuIntro():
    global pacmenu,ghostMenu1,ghostMenu2,ghostMenu3,ghostMenu4

    pacmenu=Turtle()
    pacmenu.penup()
    pacmenu.goto(0,-150)
    pacmenu.shape("img/pacpac0.gif")
    
    ghostMenu1=Turtle()
    ghostMenu1.up()
    ghostMenu1.goto(-60,-150)
    ghostMenu1.shape("img/fantome_rouge.gif")
    
    ghostMenu2=Turtle()
    ghostMenu2.up()
    ghostMenu2.goto(-90,-150)
    ghostMenu2.shape("img/fantome_rose.gif")
    
    ghostMenu3=Turtle()
    ghostMenu3.up()
    ghostMenu3.goto(-120,-150)
    ghostMenu3.shape("img/fantome_vert.gif")
    
    ghostMenu4=Turtle()
    ghostMenu4.up()
    ghostMenu4.goto(-150,-150)
    ghostMenu4.shape("img/fantome_bleu.gif")
                   
    
##############################################################
#                 affiche la carte                           #  
##############################################################   

def fondDeCarte():
    tracer(False)
    with open(niveau,"r") as carte :
        carte=carte.read().split("\n")
        i=0
        for ligne in carte :
            element=ligne.split(" ")
            j=0
            for case in element:
                goto(-300+30*j,300-30*i)
                if case == "v0":
                    shape("img/v0.gif")
                    stamp()
                elif case == "v1":
                    shape("img/v1.gif")
                    stamp()
                elif case == "m1":
                    shape("img/m1.gif")
                    stamp()
                elif case == "m2":
                    shape("img/m2.gif")
                    stamp()
                elif case == "m3":
                    shape("img/m3.gif")
                    stamp()
                elif case == "m4":
                    shape("img/m4.gif")
                    stamp()
                elif case == "m5":
                    shape("img/m5.gif")
                    stamp()
                elif case == "m6":
                    shape("img/m6.gif")
                    stamp()
                elif case == "m7":
                    shape("img/m7.gif")
                    stamp()
                elif case == "m8":
                    shape("img/m8.gif")
                    stamp()
                elif case == "m9":
                    shape("img/m9.gif")
                    stamp()
                elif case == "ma":
                    shape("img/ma.gif")
                    stamp()
                elif case == "mi":
                    shape("img/mi.gif")
                    stamp()
                elif case == "c1":
                    shape("img/c1.gif")
                    stamp()
                elif case == "c2":
                    shape("img/c2.gif")
                    stamp()
                elif case == "c3":
                    shape("img/c3.gif")
                    stamp()
                elif case == "c4":
                    shape("img/c4.gif")
                    stamp()
                j=j+1
            i=i+1
    update()
    
##############################################################
#            vie/défaite/gagnant                            #  
##############################################################

def afficherVieRest():
    global vie,vie1,vie2
    tracer(True)
    speed("fast")
    vie=Turtle()
    vie.penup()
    vie.shape("img/vie.gif")
    vie.goto(-270,-330)
    vie1=Turtle()
    vie1.penup()
    vie1.shape("img/vie.gif")
    vie1.goto(-240,-330)
    vie2=Turtle()
    vie2.penup()
    vie2.shape("img/vie.gif")
    vie2.goto(-210,-330)
    tracer(False)
    
def vieRest():
    global vie,vie1,vie2,PV
    if PV==2:
        vie2.fd(485)
    elif PV==1:
        vie1.fd(485)
    elif PV==0:
        vie.fd(485)
        
def defaite(): 
    global PV
    if PV==0:
        ghost_1.goto(0,0)
        ghost_2.goto(0,0)
        ghost_3.goto(0,0)
        ghost_4.goto(0,0)
        ghost_1.fd(0)
        ghost_2.fd(0)
        ghost_3.fd(0)
        ghost_4.fd(0)
        sc.register_shape("img/gameover.gif")
        gameOver=Turtle()
        gameOver.penup()
        gameOver.goto(0,-150)
        gameOver.shape("img/gameover.gif")
        gameOver.stamp()
        winsound.PlaySound("sounds/gameOver.wav", winsound.SND_FILENAME)
        main()
        return

    else:
        return

def gagner():
    global pions,vitesse,vitesseFANT
    for pion in pions:
        if pion.isvisible() == True:
            return True
    vitesse=0
    vitesseFANT=0
    sc.register_shape("img/Gagner.gif")
    Gagner=Turtle()
    Gagner.penup()
    Gagner.goto(0,-150)
    Gagner.shape("img/Gagner.gif")
    Gagner.stamp()    
    return False
    

##############################################################
#               gère les déplacements                        #  
##############################################################

def avancer():
    global vitesse,pas
    vitesse = pas

def gauche():
    global vitesse,pacman
    pacman.penup()
    tmp=vitesse
    vitesse=0
    pacman.lt(90)
    avancer()
    
def droite():
    global vitesse, pacman
    pacman.penup()
    tmp=vitesse
    vitesse=0
    pacman.lt(-90)
    avancer()

def mvtGhost():
    global ghost_1,ghost_2,ghost_3,ghost_4,vitesseFANT
    ghost_1.fd(vitesseFANT)
    collisionGhost1()
    ghost_2.fd(vitesseFANT)
    collisionGhost2()
    ghost_3.fd(vitesseFANT)
    collisionghost_3()
    ghost_4.fd(vitesseFANT)
    collisionghost_4()
    
##############################################################
#                   gère les collisions                      #  
##############################################################

def pointBlanc():
    global Pblanc,pions,cordpions
    Pblanc=Turtle()
    Pblanc.shape("img/Pblanc.gif")
    with open(niveau,"r") as carte :
        carte=carte.read().split("\n")
        i=0
        for ligne in carte :
            element=ligne.split(" ")
            j=0
            for case in element:
                if case== "v0":
                    Pblanc.up()
                    cordpions.append( XYtoIJ(Pblanc.xcor(),Pblanc.ycor()))
                    Pblanc.goto(-300+30*j,300-30*i)
                    pions.append(Pblanc.clone())
                j=j+1
            i=i+1
        

def detruirepointBlanc():
    global pacman,i,j,pions,cordpions,Pblanc
    cordpacman= XYtoIJ(pacman.xcor(),pacman.ycor())
    cordPblanc= XYtoIJ(Pblanc.xcor(),Pblanc.ycor())
    for pion in pions:
        cordpion= XYtoIJ(pion.xcor(),pion.ycor())
        if cordpacman==cordpion:
            pion.ht()
        elif cordpacman==cordPblanc:
            Pblanc.ht()
        
def Obstacle():
    global mur,murs,cordmurs
    mur=Turtle()
    mur.shape()
    mur.ht()
    with open(niveau,"r") as carte :
        carte=carte.read().split("\n")
        i=0
        for ligne in carte :
            element=ligne.split(" ")
            j=0
            for case in element:
                if case== "m1" or case== "m2"or case== "m3"or case== "m4"or case== "m5"\
                    or case== "m6"or case== "m7"or case== "m8"or case== "m9"or case== "ma"\
                    or case== "c1"or case== "c2"or case== "c3"or case== "c4"or case== "mi":
                    mur.up()
                    cordmurs.append( XYtoIJ(mur.xcor(),mur.ycor()))
                    mur.goto(-300+30*j,300-30*i)
                    murs.append(mur.clone())
                j=j+1             
            i=i+1
        update()

def collision():
    global pacman,cordmurs,vitesse
    a=0
    b=0
    angle=pacman.heading()
    if angle==0.0:
        a=30
        pacman.shape("img/pacpac0.gif")
    elif angle==90.0:
        b=30
        pacman.shape("img/pacpac90.gif")
    elif angle==180.0:
        a=-30
        pacman.shape("img/pacpac180.gif")
    elif angle==270.0:
        b=-30
        pacman.shape("img/pacpac270.gif")
    cordpacman= XYtoIJ(pacman.xcor()+a,pacman.ycor()+b)
    if cordpacman in cordmurs:
        vitesse=0

        

def PacpacVSFantome():
    global pacman,ghost_1,ghost_2,ghost_3,ghost_4,PV,vitesse
    
    cordghost_1= ghost_1.xcor(),ghost_1.ycor()
    cordghost_2= ghost_2.xcor(),ghost_2.ycor()
    cordghost_3= ghost_3.xcor(),ghost_3.ycor()
    cordghost_4= ghost_4.xcor(),ghost_4.ycor()
    pacmanPos=pacman.xcor(),pacman.ycor()

    if pacman.xcor()-ghost_1.xcor()<=30 and pacman.ycor()-ghost_1.ycor()<=30 and pacman.xcor()-ghost_1.xcor()>=-30 and pacman.ycor()-ghost_1.ycor()>=-30:
        PV=PV-1
        vitesse=0
        pacman.goto(0,-150)
    if pacman.xcor()-ghost_2.xcor()<=30 and pacman.ycor()-ghost_2.ycor()<=30 and pacman.xcor()-ghost_2.xcor()>=-30 and pacman.ycor()-ghost_2.ycor()>=-30:
        PV=PV-1
        vitesse=0
        pacman.goto(0,-150)
    if pacman.xcor()-ghost_3.xcor()<=30 and pacman.ycor()-ghost_3.ycor()<=30 and pacman.xcor()-ghost_3.xcor()>=-30 and pacman.ycor()-ghost_3.ycor()>=-30:
        PV=PV-1
        vitesse=0
        pacman.goto(0,-150)
    if pacman.xcor()-ghost_4.xcor()<=30 and pacman.ycor()-ghost_4.ycor()<=30 and pacman.xcor()-ghost_4.xcor()>=-30 and pacman.ycor()-ghost_4.ycor()>=-30:
        PV=PV-1
        vitesse=0
        pacman.goto(0,-150)

        
def collisionGhost1():
    global ghost_1,cordmurs
    cordghost_1= XYtoIJ(ghost_1.xcor(),ghost_1.ycor())
    if cordghost_1 in cordmurs:
        ghost_1.fd(-30)
        Deplacement=randint(0,2)
        if Deplacement==0:   
            ghost_1.lt(90)
        elif Deplacement==1:
            ghost_1.rt(90)
        elif Deplacement==2:
            ghost_1.rt(180)

def collisionGhost2():
    global ghost_2,cordmurs
    cordghost_2= XYtoIJ(ghost_2.xcor(),ghost_2.ycor())
    if cordghost_2 in cordmurs:
        ghost_2.fd(-30)
        Deplacement=randint(0,2)
        if Deplacement==0:   
            ghost_2.lt(90)
        elif Deplacement==1:
            ghost_2.rt(90)
        elif Deplacement==2:
            ghost_2.rt(180)

def collisionghost_3():
    global ghost_3,cordmurs
    cordghost_3= XYtoIJ(ghost_3.xcor(),ghost_3.ycor())
    if cordghost_3 in cordmurs:
        ghost_3.fd(-30)
        Deplacement=randint(0,2)
        if Deplacement==0:   
            ghost_3.lt(90)
        elif Deplacement==1:
            ghost_2.rt(90)
        elif Deplacement==2:
            ghost_3.rt(180)

def collisionghost_4():
    global ghost_4,cordmurs
    cordghost_4= XYtoIJ(ghost_4.xcor(),ghost_4.ycor())
    if cordghost_4 in cordmurs:
        ghost_4.fd(-30)
        Deplacement=randint(0,2)
        if Deplacement==0:   
            ghost_4.lt(90)
        elif Deplacement==1:
            ghost_4.rt(90)
        elif Deplacement==2:
            ghost_2.rt(180)
                    
##############################################################
#               fantomes                                     #  
##############################################################                   

def fantome():
    global ghost_1,ghost_2,ghost_3,ghost_4,vitesse,pas
    vitesse=pas
    
    ghost_1=Turtle()
    ghost_1.up()
    ghost_1.shape("img/fantome_rouge.gif")
    ghost_1.goto(0,0)
    ghost_1.lt(90)
    ghost_1.fd(90)
    
    ghost_2=Turtle()
    ghost_2.up()
    ghost_2.shape("img/fantome_rose.gif")
    ghost_2.goto(0,0)
    ghost_2.lt(90)
    ghost_2.fd(60)
    
    ghost_3=Turtle()
    ghost_3.up()
    ghost_3.shape("img/fantome_vert.gif")
    ghost_3.goto(0,0)
    ghost_3.lt(90)
    ghost_3.fd(150)

    ghost_4=Turtle()
    ghost_4.up()
    ghost_4.shape("img/fantome_bleu.gif")
    ghost_4.goto(0,0)
    ghost_4.lt(90)
    ghost_4.fd(120)

##############################################################
#               Programme principal                          #  
##############################################################

def anime():
    global pacman
    ecoute()
    pacman.penup()
    collision()
    pacman.fd(vitesse)
    update()
    detruirepointBlanc()
    vieRest()   
    mvtGhost()
    defaite()
    gagner()
    PacpacVSFantome()
    sc.ontimer(anime,vitessePAC)

def quitter():
    sc.bye()

def ecoute():    
    onkeypress(avancer,key="Up")
    onkeypress(gauche,key="Left")
    onkeypress(droite,key="Right")
    sc.onkeypress(main,key='F5')
    onkeypress(quitter,"Escape")
    listen()

def main():
    sc.reset()
    menuCarte()
    sc.onkeypress(main,key='F5')
    sc.listen()

if __name__=='__main__':
    print(main())
    mainloop()
