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
def printArrayState(array,n,m):
    for i in range(n):
        for j in range(m):
            print(array[i][j].getIsBomb(),end=" ")
        print()

def printMinesAround(array,n,m):
    for i in range(n):
        for j in range(m):
            print(array[i][j].getMinesAround(),end=" ")
        print()

'''Tymczasowe zainicjowanie zmiennych które w przyszłosci będą wprowadzone w textboxie'''
n=10
m=10
bombs=10

'''Ustalenie wymiarów okna'''
if n <8 and m<8:
    fieldHeight = 100
    fieldWidth = 100
else:
    fieldHeight=60
    fieldWidth=60
topBarHeight=75

height=n*fieldHeight+topBarHeight
width=m*fieldWidth

resolution = (width, height)
window = pygame.display.set_mode(resolution, DOUBLEBUF)
window.fill((255, 255, 255))



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

class Square():
    def __init__(self,x,y,height,width,clicked,isVisible,image):
        '''
        x,y - koordynaty pola
        height,width - wymiary pola
        clicked - 0-nie,1-LPM,2-PPMx1,3-PPMx2
        isVisible - czy odkryte?
        '''
        self._x = x
        self._y = y
        self._height = height
        self._width = width
        self._clicked = clicked
        self._isVisible = isVisible
        self._image = image
    def getPxX(self):
        return self._x*self._height
    def getPxY(self):
        return self._y*self._width
    def draw(self,window):
        window.blit(numbers[0], (self.getPxX, self.getPxY))

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif True :
            pass


    pygame.display.update()


array=getMatrix(n,m,bombs)
printArrayState(array,n,m)
printMinesAround(array,n,m)