'''Importowane biblioteki'''
import pygame
import logic.fields as fd
import graphics.icons as ic
import graphics.iconsBig as icB
import graphics.windows as wd
import graphics.squares as sq

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
    gameWindow.resetStarted()
    gameWindow.getTimer().updateTime(0,gameWindow.getScreen())
    fd.Field.flaggedBombCount = 0
    sq.Square.visibleCount = 0
    sq.Square.flaggedCount = 0
    minesweeper(n,m,bombs)

def minesweeper(n,m,bombs):

    fields=fd.getMatrix(n,m,bombs)
    gameWindow.resetSquares()
    squares = gameWindow.getSquares()

    timer=pygame.time.Clock()
    startTime=0
    clickTime=0
    gameWindow.drawScene()
    pygame.display.flip()
    run=True
    """Pomoc przy debugowaniu:"""
    printArrayState(fields, n, m)
    printMinesAround(fields, n, m)

    xyzzySequence = [False, False, False, False, False]
    while run:

        for event in pygame.event.get():
            '''LAMBDA #4'''
            if (lambda ev: event.type == ev)(pygame.QUIT):
                #run = False
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


                if gameWindow.getCat().getCat().collidepoint(event.pos):
                    run = False
                    reset()
                for i in range(n):
                    for j in range(m):
                        if squares[i][j].getRect().collidepoint(event.pos):
                            if gameWindow.squares[0][0].visibleCount == 0 and not gameWindow.getStarted():
                                # print(gameWindow.squares[0][0].visibleCount)
                                startTime = pygame.time.get_ticks()
                                clickTime = pygame.time.get_ticks()
                                time = int(startTime - clickTime)
                                gameWindow._timer.updateTime(time, gameWindow.getScreen())
                                gameWindow.getStarted()
                            gameWindow.reveal(fields,i,j,bombs)
                            break
                        elif squares[i][j].getClicked()==2:
                                """Celowe ominiecie reakcji ponieważ oflagowane pole nie moze byc klikniete"""
                                pass
                        elif squares[i][j].getClicked()==3:
                                """Celowe ominiecie reakcji ponieważ pole z pytajnikiem nie moze byc klikniete"""
                                pass

                '''LAMBDA #7'''
            elif (lambda ev,evb: event.type == ev and event.button==evb)(pygame.MOUSEBUTTONDOWN,3):

                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        if squares[i][j].getRect().collidepoint(event.pos):
                                if not gameWindow.getStarted() and not gameWindow.squares[0][0].visibleCount == n*m:
                                    # print(gameWindow.squares[0][0].visibleCount)
                                    startTime = pygame.time.get_ticks()
                                    clickTime = pygame.time.get_ticks()
                                    time = int(startTime - clickTime)
                                    gameWindow._timer.updateTime(time, gameWindow.getScreen())
                                    gameWindow.setStarted()
                                if gameWindow.getStarted():
                                    if squares[i][j].getClicked() == 0:
                                        fields[i][j].incBombFlagged()
                                        if squares[i][j].getSize()>60:
                                            squares[i][j].setImage(icB.flag)
                                        else:
                                            squares[i][j].setImage(ic.flag)
                                        squares[i][j].draw(screen)
                                        squares[i][j].setClicked(2)
                                        gameWindow.checkIfWin(fields, i, j,bombs)
                                        pygame.display.flip()

                                    elif squares[i][j].getClicked() == 2:
                                        fields[i][j].decBombFlagged()
                                        if squares[i][j].getSize()>60:
                                            squares[i][j].setImage(icB.qmark)
                                        else:
                                            squares[i][j].setImage(ic.qmark)
                                        #squares[i][j].setImage(ic.qmark)
                                        squares[i][j].draw(screen)
                                        squares[i][j].setClicked(3)
                                        pygame.display.flip()
                                    elif squares[i][j].getClicked() == 3:
                                        if squares[i][j].getSize()>60:
                                            squares[i][j].setImage(icB.default)
                                        else:
                                            squares[i][j].setImage(ic.default)
                                        #squares[i][j].setImage(ic.default)
                                        squares[i][j].draw(screen)
                                        squares[i][j].setClicked(0)
                                        gameWindow.checkIfWin(fields, i, j,bombs)
                                        pygame.display.update()
                    else:
                           pass
        screen.fill((255, 255, 255))
        gameWindow.drawScene()

        if  gameWindow.getStarted() and gameWindow.squares[0][0].visibleCount!=0 and gameWindow.squares[0][0].visibleCount!=n*m:
            #print(gameWindow.getStarted()," ", gameWindow.squares[0][0].visibleCount, " ", n*m)
            clickTime = pygame.time.get_ticks()
            time = int(clickTime-startTime)//1000
            gameWindow._timer.updateTime(time, gameWindow.getScreen())
        timer.tick(60)

if __name__ == '__main__':
    n,m,bombs=wd.configuration()
    topBarHeight=75

    gameWindow = wd.GameWindow(n, m, topBarHeight)
    gameWindow.setWindow()
    window=gameWindow.getWindow()
    gameWindow.setScreen()
    screen=gameWindow.getScreen()
    pygame.display.set_caption("Saper")
    pygame.display.set_icon(ic.icon)
    squareHeight=gameWindow.getSquareH()
    squareWidth=gameWindow.getSquareW()

    minesweeper(n,m,bombs)