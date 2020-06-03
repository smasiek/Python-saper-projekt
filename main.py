'''Importowane biblioteki'''
import random
import pygame
import logic.fields as fd
import graphics.icons as ic
import graphics.windows as wd
import graphics.squares as sq
#from graphics.windows import configuration as conf
#from pygame.locals import *
pygame.init()

def printArrayState(array,n,m):
    for i in range(n):
        for j in range(m):
            print(array[i][j].isBomb(), end=" ")
        print()

def printMinesAround(array,n,m):
    for i in range(n):
        for j in range(m):
            print(array[i][j].getMinesAround(),end=" ")
        print()

def reset():
    gameWindow.clearWindow()
    fd.Field.flaggedBombCount = 0
    sq.Square.visibleCount = 0
    sq.Square.flaggedCount = 0
    minesweeper(n,m,bombs)

def minesweeper(n,m,bombs):

    fields=fd.getMatrix(n,m,bombs)
    gameWindow.resetSquares()
    squares = gameWindow.getSquares()
    gameWindow.drawScene()

    pygame.display.update()
    run=True
    """Pomoc przy debugowaniu:"""
    printArrayState(fields, n, m)
    printMinesAround(fields, n, m)

    xyzzySequence = [False, False, False, False, False]
    while run:

        for event in pygame.event.get():
            '''LAMBDA #4'''
            if (lambda ev: event.type == ev)(pygame.QUIT):
                run = False
                pygame.quit()
                '''LAMBDA #5'''
            elif (lambda ev: event.type == ev)(pygame.KEYDOWN):
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_r: # TO W PRZYSZLOSCI ZAMIENIC NA KLIKNIECIE W PRZYCISK a nie w klawiature
                    run = False
                    reset()

                elif keys[pygame.K_x]:
                    '''xyzzy event'''
                    xyzzySequence[0]=True
                elif keys[pygame.K_y] and xyzzySequence[0]== True :
                    #print(xyzzySequence[0])
                    xyzzySequence[0] = False
                    xyzzySequence[1]=True
                    #print("kod uruchomiony")
                elif keys[pygame.K_z] and xyzzySequence[1]==True:
                    xyzzySequence[1] = False
                    xyzzySequence[2] = True
                    #print("kod uruchomiony")
                elif keys[pygame.K_z] and xyzzySequence[2]==True:
                    xyzzySequence[2] = False
                    xyzzySequence[3] = True
                    #print("kod")
                elif keys[pygame.K_y] and xyzzySequence[3]==True:
                    xyzzySequence[3] = False
                    xyzzySequence[4] = True
                    gameWindow.xyzzy(fields)
                elif event.key != pygame.K_x or event.key != pygame.K_y or event.key != pygame.K_z:
                    print("inny przycisk klikniety")
                    print(xyzzySequence)
                    for i in range(len(xyzzySequence)):
                        xyzzySequence[i]=False
                    print(xyzzySequence)
                '''LAMBDA #6'''
            elif (lambda ev,evb: event.type == ev and event.button==evb)(pygame.MOUSEBUTTONDOWN,1):
                #isBreak=False
                for i in range(n):
                    for j in range(m):
                        if squares[i][j].getRect().collidepoint(event.pos):
                            gameWindow.reveal(fields,i,j,bombs)
                            #isBreak=True
                            break
                        elif squares[i][j].getClicked()==2:
                                """Celowe ominiecie reakcji ponieważ oflagowane pole nie moze byc klikniete"""
                                pass
                        elif squares[i][j].getClicked()==3:
                                """Celowe ominiecie reakcji ponieważ pole z pytajnikiem nie moze byc klikniete"""
                                pass
                    #if isBreak:
                        #break
                '''LAMBDA #7'''
            elif (lambda ev,evb: event.type == ev and event.button==evb)(pygame.MOUSEBUTTONDOWN,3):
                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        if squares[i][j].getRect().collidepoint(event.pos):
                            if squares[i][j].getClicked() == 0:
                                fields[i][j].incBombFlagged()
                                squares[i][j].setImage(ic.flag)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(2)
                                gameWindow.checkIfWin(fields, i, j,bombs)
                                pygame.display.update()

                            elif squares[i][j].getClicked() == 2:
                                fields[i][j].decBombFlagged()
                                squares[i][j].setImage(ic.qmark)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(3)
                                pygame.display.update()
                            elif squares[i][j].getClicked() == 3:
                                squares[i][j].setImage(ic.default)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(0)
                                gameWindow.checkIfWin(fields, i, j,bombs)
                                pygame.display.update()
                    else:
                           pass


n,m,bombs=wd.configuration()
topBarHeight=75

gameWindow = wd.GameWindow(n, m, topBarHeight)
gameWindow.setWindow()
window=gameWindow.getWindow()
gameWindow.setScreen()
screen=gameWindow.getScreen()
squareHeight=gameWindow.getSquareH()
squareWidth=gameWindow.getSquareW()


minesweeper(n,m,bombs)