'''Importowane biblioteki'''
import random
import pygame
from pygame.locals import *
pygame.init()

class Field:
    '''
    Stworzenie Pola jako klasy posiadającej odpowiednie pola
    '''

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
    def getIsBomb(self):
        return self._isBomb
    def getMinesAround(self):
        return self._minesAround

class Square():
    def __init__(self,x,y,height,width,clicked,isVisible,image):
        '''
        x,y - koordynaty pola
        height,width - wymiary pola
        clicked - 0-nie,1-LPM,2-PPMx1,3-PPMx2
        isVisible - czy odkryte?
        '''
        self._rect=pygame.rect.Rect(x,y+75,height,width)
        self._x = x
        self._y = y+75
        self._height = height
        self._width = width
        self._clicked = clicked
        self._isVisible = isVisible
        self._image = image

    def getPxX(self):
        return int(self._x)

    def getPxY(self):
        return int(self._y) #75 = topBarHeight

    def draw(self,window):
        window.blit(self._image, (self.getPxX(),self.getPxY()))

    def setImage(self,image):
        self._image=image

    def setClicked(self,click):
        self._clicked=click;

    def getClicked(self):
        return self._clicked

def flood(squares,fields,numbers,screen,i,j,n,m,isFlood):

    tab=[-1,0,1]
    for l in tab:
        for k in tab:
            print(i+k," cos tam ",j+l)
            if (k!=0 or l!=0) and ( (i+k>=0 and j+l<m) and (i+k<n and j+l<m) and(i+k>=0 and j+l>=0) and (i+k>=0 and j+l<m)):
                if squares[i+k][j+l].getClicked() == 0:
                    if not fields[i + k][j + l].getIsBomb():
                        squares[i + k][j + l].setImage(numbers[fields[i + k][j + l].getMinesAround()])
                        squares[i + k][j + l].draw(screen)
                        squares[i + k][j + l].setClicked(1)
                        if isFlood==True:
                            if fields[i + k][j + l].getMinesAround() == 0:

                                flood(squares, fields, numbers, screen, i + k, j + l, n, m,True)
                            else:
                                flood(squares, fields, numbers, screen, i + k, j + l, n, m, False)
                        #elif:
                            #pass







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
    possibilities=[[[i,j]for j in range(m)]for i in range(n)]

    for i in range(bombs):
        '''Uzupelnianie minami'''

        chosen = random.choice(random.choice(possibilities))
        array[chosen[0]][chosen[1]].setIsBomb()
        '''Skorygowanie pola minyNaOkoło'''

        if chosen[0] - 1 >= 0 and chosen[1] - 1 >= 0:
            array[chosen[0] - 1][chosen[1] - 1].incMinesAround()

        if chosen[1]-1 >= 0:
            array[chosen[0]][chosen[1]-1].incMinesAround()

        if chosen[0] + 1 < n and chosen[1] - 1 >= 0:
            array[chosen[0] + 1][chosen[1] - 1].incMinesAround()

        if chosen[0] - 1 >= 0:
            array[chosen[0]-1][chosen[1]].incMinesAround()

        if chosen[0] + 1 < n:
            array[chosen[0]+1][chosen[1]].incMinesAround()

        if chosen[0] - 1 >= 0 and chosen[1] + 1 < m:
            array[chosen[0] - 1][chosen[1] + 1].incMinesAround()

        if chosen[1] + 1 < m:
            array[chosen[0]][chosen[1]+1].incMinesAround()

        if chosen[0] + 1 < n and chosen[1] + 1 < m:
            array[chosen[0] + 1][chosen[1] + 1].incMinesAround()

    return array

def drawScene(squares,window):

    for i in range(len(squares)):
        for j in range(len(squares[i])):
            squares[i][j].draw(window)

def printArrayState(array,n,m):
    for i in range(n):
        for j in range(m):
            print(array[i][j].getIsBomb(),end=" ")
        print()



def reset():
    minesweeper(n,m,bombs)
'''Tymczasowe zainicjowanie zmiennych które w przyszłosci będą wprowadzone w textboxie'''
n=15
m=15
bombs=40
def minesweeper(n,m,bombs):
    '''Ustalenie wymiarów okna'''
    if n <8 and m<8:
        squareHeight = 100
        squareWidth = 100
    else:
        squareHeight=60
        squareWidth=60
    topBarHeight=75

    height= n * squareHeight + topBarHeight
    width= m * squareWidth
    resolution = (width, height)
    window = pygame.display.set_mode(resolution, DOUBLEBUF)
    window.fill((255, 255, 255))
    screen = pygame.display.get_surface()

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
    flag=pygame.image.load("icons\\flag.png")
    qmark=pygame.image.load("icons\\qmark.png")
    default=pygame.image.load("icons\\def.png")

    numbers=[zero,one,two,three,four,five,six,seven,eight]

    fields=getMatrix(n,m,bombs)

    squares=[[Square(i*squareHeight,j*squareWidth,squareHeight,squareWidth,0,False,default)for j in range(m)]for i in range(n)]

    drawScene(squares, screen)
    pygame.display.update()
    run=True
    """@DOWN do usuniecia - kontrola czy dobrze wyswietlaja sie cyferki"""
    printArrayState(fields, n, m)
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # TO W PRZYSZLOSCI ZAMIENIC NA KLIKNIECIE W PRZYCISK a nie w klawiature
                    run = False
                    reset()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        r=pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                        if squares[i][j]._rect.colliderect(r):
                            if squares[i][j].getClicked()==0:
                                if fields[i][j].getIsBomb():
                                    squares[i][j].setImage(bomb)
                                    squares[i][j].draw(screen)
                                    squares[i][j].setClicked(1)
                                    """DODAC TUTAJ FUNKCJE ZAKONCZENIA GRY"""
                                    pygame.display.update()
                                else:
                                    squares[i][j].setImage(numbers[fields[i][j].getMinesAround()])
                                    squares[i][j].draw(screen)
                                    squares[i][j].setClicked(1)
                                    """
                                     DODAC TUTAJ WARUNEK SPRAWDZAJACY WYGRANA
                                        TAK: DODAC TUTAJ FUNKCJE ZAKONCZENIA GRY
                                        NIE: PASS
                                    """
                                    if fields[i][j].getMinesAround() == 0:
                                        flood(squares, fields, numbers, screen, i, j,n,m,True)
                                    pygame.display.update()
                            elif squares[i][j].getClicked()==2:
                                """Celowe ominiecie reakcji ponieważ oflagowane pole nie moze byc klikniete"""
                                pass
                            elif squares[i][j].getClicked()==3:
                                """Celowe ominiecie reakcji ponieważ pole z pytajnikiem nie moze byc klikniete"""
                                pass

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                        if squares[i][j]._rect.colliderect(r):
                            if squares[i][j].getClicked() == 0:
                                squares[i][j].setImage(flag)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(2)
                                pygame.display.update()

                            elif squares[i][j].getClicked() == 2:
                                squares[i][j].setImage(qmark)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(3)
                                pygame.display.update()
                            elif squares[i][j].getClicked() == 3:
                                squares[i][j].setImage(default)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(0)
                                pygame.display.update()
                    else:
                           pass#print(squares[i][j]._rect)
                                            #print(squares[i][j].getClicked())
                                #pygame.display.update()





minesweeper(n,m,bombs)