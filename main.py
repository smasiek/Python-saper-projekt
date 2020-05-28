'''Importowane biblioteki'''
import random
import pygame
from pygame.locals import *
pygame.init()

class Field:
    '''
    Stworzenie Pola jako klasy posiadającej odpowiednie pola
    '''
    flaggedBombCount=0
    def __init__(self,isBomb,x,y,minesAround):
        self._isBomb=isBomb
        self._x=x
        self._y=y
        self._minesAround=minesAround
    def setIsBomb(self):
        self._isBomb=True
    def setMinesAround(self,minesAround):
        self._minesAround=minesAround
    def incMinesAround(self):
        self._minesAround+=1
    def incBombFlagged(self):
        if self._isBomb:
            Field.flaggedBombCount +=1
            print("Oznaczono bombe, count", Field.flaggedBombCount)
    def decBombFlagged(self):
        if self.isBomb():
            Field.flaggedBombCount -=1
            print("Odznaczono bombe, count", Field.flaggedBombCount)
    def isBomb(self):
        return self._isBomb
    def getMinesAround(self):
        return self._minesAround

class Square():
    visibleCount=0
    flaggedCount=0
    def __init__(self,x,y,height,width,clicked,image):
        '''
        x,y - koordynaty pola
        height,width - wymiary pola
        clicked - 0-nie,1-LPM,2-PPMx1,3-PPMx2
        '''
        self._rect=pygame.rect.Rect(x,y+75,height,width)
        self._x = x+75
        self._y = y
        self._height = height
        self._width = width
        self._clicked = clicked
        self._image = image

    def getPxX(self):
        return int(self._x)

    def getPxY(self):
        return int(self._y) #75 = topBarHeight

    def draw(self,window):
        window.blit(self._image, (self.getPxY(),self.getPxX()))

    #def incVisibleCount(self):
    #    self.visibleCount+=1

    def setImage(self,image):
        self._image=image

    def setClicked(self,click):
        self._clicked=click
        if click==1:
            Square.visibleCount += 1
        if click==2:
            Square.flaggedCount += 1
        if click==0:
            Square.flaggedCount -= 1
        #print("Flagged count:" ,Square.flaggedCount)

    def getClicked(self):
        return self._clicked

    def getVisibleCount(self):
        return self.visibleCount

'''Tu zrobic funkcje ktora w okienku bedzie obslugiwala wpisywanie n i m a potem tworzenie okna, poki co z ręki:'''
n=3
m=3
bombs=5

if n < 8 and m < 8:
    squareHeight = 100
    squareWidth = 100
else:
    squareHeight = 60
    squareWidth = 60
topBarHeight = 75

height = n * squareHeight + topBarHeight
width = m * squareWidth
resolution = (width, height)
window = pygame.display.set_mode(resolution, DOUBLEBUF)
window.fill((255, 255, 255))
screen = pygame.display.get_surface()


'''Koniec funkcji'''


zero=pygame.image.load("icons\\blank.png")
one=pygame.image.load("icons\\1.png")
two=pygame.image.load("icons\\2.png")
three=pygame.image.load("icons\\3.png")
four=pygame.image.load("icons\\4.png")
five=pygame.image.load("icons\\5.png")
six=pygame.image.load("icons\\6.png")
seven=pygame.image.load("icons\\7.png")
eight=pygame.image.load("icons\\8.png")
bomb=pygame.image.load("icons\\bomb.png")
xyzz=pygame.image.load("icons\\xyzzy.png")
flaggedxyzz=pygame.image.load("icons\\flaggedxyzzy.png")
flag=pygame.image.load("icons\\flag.png")
qmark=pygame.image.load("icons\\qmark.png")
default=pygame.image.load("icons\\def.png")

numbers=[zero,one,two,three,four,five,six,seven,eight]


'''Metody klasy plansza, narazie muszą być tu bo inaczej nie będą sie widzieć na wzajem i muszą widziec squares'''
def endGame(squares,fields):
    for i in range(n):
        for j in range(m):
            if squares[i][j].getClicked() == 0 or squares[i][j].getClicked() == 2 or squares[i][j].getClicked() == 3:
                if fields[i][j].isBomb():
                    squares[i][j].setImage(bomb)
                    squares[i][j].draw(screen)
                    squares[i][j].setClicked(1)
                else:
                    squares[i][j].setImage(numbers[fields[i][j].getMinesAround()])
                    squares[i][j].draw(screen)
                    squares[i][j].setClicked(1)
    pygame.display.update()

def checkIfWin(squares,fields,i,j):
    if (m*n)-squares[i][j].visibleCount<=bombs:
        print('win by click')
        return endGame(squares, fields)
    if Field.flaggedBombCount==bombs and Square.flaggedCount == bombs:
        print('win by flagged')
        return endGame(squares, fields)
'''koniec metod klasy plansza'''


def reveal(squares,fields,i,j):
    if squares[i][j].getClicked() == 0:
        if fields[i][j].isBomb():
            squares[i][j].setImage(bomb)
            squares[i][j].draw(screen)
            squares[i][j].setClicked(1)
            endGame(squares, fields)
            """DODAC TUTAJ FUNKCJE ZAKONCZENIA GRY"""
            pygame.display.update()
        else:
            squares[i][j].setImage(numbers[fields[i][j].getMinesAround()])
            squares[i][j].draw(screen)
            #squares[i][j].incVisibleCount()
            squares[i][j].setClicked(1)
            """
             DODAC TUTAJ WARUNEK SPRAWDZAJACY WYGRANA
                TAK: DODAC TUTAJ FUNKCJE ZAKONCZENIA GRY
                NIE: PASS
            """
            if fields[i][j].getMinesAround() == 0:
                flood(squares, fields, numbers, screen, i, j, n, m)
            checkIfWin(squares, fields, i, j)
            pygame.display.update()

def flood(squares,fields,numbers,screen,i,j,n,m):

    tab=[-1,0,1]
    for l in tab:
        for k in tab:
            ii=i+l
            jj=j+k
            if ii>-1 and ii<n and jj>-1 and jj<m:
                if not fields[ii][jj].isBomb():
                   reveal(squares,fields,ii,jj)


def xyzzy(squares,fields):
    for i in range(n):
        for j in range(m):
            if fields[i][j].isBomb():
                if not squares[i][j].getClicked()==2:
                    squares[i][j].setImage(xyzz)
                    squares[i][j].draw(screen)
                else:
                    squares[i][j].setImage(flaggedxyzz)
                    squares[i][j].draw(screen)
    pygame.display.update()


'''
Stworzenie tablicy reprezentujacej plansze
'''

def getMatrix(n,m,bombs):
    '''
    :param n: 1st wymiar planszy
    :param m: 2nd wymiar planszy
    :param bombs: ilosc bomb
    :return: plansza true/false
    '''
    array=[[Field(False,i,j,0) for j in range(m)]for i in range(n)]
    possibilities=[[i,j] for j in range(m) for i in range(n)]

    for i in range(bombs):
        '''Uzupelnianie minami'''

        chosen = random.choice(possibilities)
        print(chosen)
        possibilities.remove(chosen)

        array[chosen[0]][chosen[1]].setIsBomb()
        '''Skorygowanie pola minyNaOkoło'''

        if (chosen[0] - 1) >= 0 and (chosen[1] - 1) >= 0 and not array[chosen[0] - 1][chosen[1] - 1].isBomb() :
            array[chosen[0] - 1][chosen[1] - 1].incMinesAround()

        if (chosen[1]-1) >= 0 and not array[chosen[0]][chosen[1]-1].isBomb() :
            array[chosen[0]][chosen[1]-1].incMinesAround()

        if chosen[0] + 1 < n and chosen[1] - 1 >= 0 and not array[chosen[0] + 1][chosen[1] - 1].isBomb() :
            array[chosen[0] + 1][chosen[1] - 1].incMinesAround()

        if chosen[0] - 1 >= 0 and not array[chosen[0]-1][chosen[1]].isBomb() :
            array[chosen[0]-1][chosen[1]].incMinesAround()

        if chosen[0] + 1 < n and not array[chosen[0]+1][chosen[1]].isBomb() :
            array[chosen[0]+1][chosen[1]].incMinesAround()

        if chosen[0] - 1 >= 0 and chosen[1] + 1 < m and not array[chosen[0] - 1][chosen[1] + 1].isBomb() :
            array[chosen[0] - 1][chosen[1] + 1].incMinesAround()

        if chosen[1] + 1 < m and not array[chosen[0]][chosen[1]+1].isBomb() :
            array[chosen[0]][chosen[1]+1].incMinesAround()

        if chosen[0] + 1 < n and chosen[1] + 1 < m and not array[chosen[0] + 1][chosen[1] + 1].isBomb() :
            array[chosen[0] + 1][chosen[1] + 1].incMinesAround()

    return array

def drawScene(squares,window):

    for i in range(len(squares)):
        for j in range(len(squares[i])):
            squares[i][j].draw(window)

def printArrayState(array,n,m):
    for i in range(n):
        for j in range(m):
            print(array[i][j].isBomb(), end=" ")
        print()

def printMinesAround(array,n,m):
    for i in range(n):
        for j in range(n):
            print(array[i][j].getMinesAround(),end=" ")
        print()


def reset():
    window.fill((255, 255, 255))
    Field.flaggedBombCount = 0
    Square.visibleCount = 0
    Square.flaggedCount = 0
    minesweeper(n,m,bombs)
'''Tymczasowe zainicjowanie zmiennych które w przyszłosci będą wprowadzone w textboxie'''

def minesweeper(n,m,bombs):
    '''Ustalenie wymiarów okna'''




    fields=getMatrix(n,m,bombs)
    squares=[[Square(i*squareHeight,j*squareWidth,squareHeight,squareWidth,0,default)for j in range(m)]for i in range(n)]

    drawScene(squares, screen)
    pygame.display.update()
    run=True
    """@DOWN do usuniecia - kontrola czy dobrze wyswietlaja sie cyferki"""
    printArrayState(fields, n, m)
    printMinesAround(fields, n, m)
    xyzzySequence = [False, False, False, False, False]
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_r: # TO W PRZYSZLOSCI ZAMIENIC NA KLIKNIECIE W PRZYCISK a nie w klawiature
                    run = False
                    reset()

                elif keys[K_x]:
                    '''xyzzy event'''
                    xyzzySequence[0]=True
                    #print(xyzzySequence[0])
                    #print("kod uruchomiony")

#                    if event.type == pygame.KEYUP:
 #                       if event.type == pygame.KEYDOWN:
                elif keys[K_y] and xyzzySequence[0]== True :
                    #print(xyzzySequence[0])
                    xyzzySequence[0] = False
                    xyzzySequence[1]=True
                    #print("kod uruchomiony")
                elif keys[K_z] and xyzzySequence[1]==True:
                    xyzzySequence[1] = False
                    xyzzySequence[2] = True
                    #print("kod uruchomiony")
                elif keys[K_z] and xyzzySequence[2]==True:
                    xyzzySequence[2] = False
                    xyzzySequence[3] = True
                    #print("kod")
                elif keys[K_y] and xyzzySequence[3]==True:
                    xyzzySequence[3] = False
                    xyzzySequence[4] = True
                    xyzzy(squares,fields)
                elif event.key != pygame.K_x or event.key != pygame.K_y or event.key != pygame.K_z:
                    print("inny przycisk klikniety")
                    print(xyzzySequence)
                    for i in range(len(xyzzySequence)):
                        xyzzySequence[i]=False
                    print(xyzzySequence)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        r=pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                        if squares[j][i]._rect.colliderect(r):
                            reveal(squares,fields,i,j)
                        elif squares[j][i].getClicked()==2:
                                """Celowe ominiecie reakcji ponieważ oflagowane pole nie moze byc klikniete"""
                                pass
                        elif squares[j][i].getClicked()==3:
                                """Celowe ominiecie reakcji ponieważ pole z pytajnikiem nie moze byc klikniete"""
                                pass

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                        if squares[i][j]._rect.colliderect(r):
                            if squares[j][i].getClicked() == 0:
                                fields[j][i].incBombFlagged()
                                squares[j][i].setImage(flag)
                                squares[j][i].draw(screen)
                                squares[j][i].setClicked(2)
                                checkIfWin(squares, fields, i, j)
                                pygame.display.update()

                            elif squares[j][i].getClicked() == 2:
                                fields[j][i].decBombFlagged()
                                squares[j][i].setImage(qmark)
                                squares[j][i].draw(screen)
                                squares[j][i].setClicked(3)
                                pygame.display.update()
                            elif squares[j][i].getClicked() == 3:
                                squares[j][i].setImage(default)
                                squares[j][i].draw(screen)
                                squares[j][i].setClicked(0)
                                checkIfWin(squares, fields, i, j)
                                pygame.display.update()
                    else:
                           pass#print(squares[i][j]._rect)
                                            #print(squares[i][j].getClicked())
                                #pygame.display.update()





minesweeper(n,m,bombs)