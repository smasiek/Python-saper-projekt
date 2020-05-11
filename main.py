'''Importowane biblioteki'''
import random


class Field:
    '''
    Stworzenie Pola jako klasy posiadającej odpowiednie pola
    '''

    def __init__(self,isBomb,x,y,clicked,minesAround,isActive):
        self._isBomb=isBomb
        self._x=x
        self._y=y
        self._clicked=clicked
        self._minesAround=minesAround
        self._isActive=isActive
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
    def getClicked(self):
        return self._clicked
    def getActive(self):
        return self._isActive


'''
Stworzenie tablicy reprezentujacej wystepowanie bomb
'''

def isBombArray(n,bombs):
    '''
    :param n: wymiar planszy
    :param bombs: ilosc bomb
    :return: plansza true/false
    '''
    array=[[Field(False,i,j,'0',0,True) for j in range(n)]for i in range(n)]
    possibilities=[[[i,j]for j in range(n)]for i in range(n)]

    for i in range(bombs):
        '''Uzupelnianie minami'''

        chosen = random.choice(random.choice(possibilities))
        array[chosen[0]][chosen[1]].setIsBomb()
        countBombs = 0
        for x in range(1):
            if chosen[0] - 1 > 0 and chosen[1] - 1 > 0:
                if not array[chosen[0] - 1][chosen[1] - 1].getIsBomb():
                    array[chosen[0] - 1][chosen[1] - 1].incMinesAround()
            if chosen[0]-1>0:
                if not array[chosen[0]-1][chosen[1]].getIsBomb():
                    array[chosen[0]-1][chosen[1]].incMinesAround()
            if chosen[0] - 1 > 0 and chosen[1] + 1 < n:
                if not array[chosen[0] - 1][chosen[1] + 1].getIsBomb():
                    array[chosen[0] - 1][chosen[1] + 1].incMinesAround()
            if chosen[1] - 1 > 0:
                if not array[chosen[0]][chosen[1] - 1].getIsBomb():
                    array[chosen[0]][chosen[1] - 1].incMinesAround()
            if chosen[1] + 1 < n:
                if not array[chosen[0]][chosen[1] + 1].getIsBomb():
                    array[chosen[0]][chosen[1] + 1].incMinesAround()
            if chosen[0] + 1 < n and chosen[1] - 1 > 0:
                if not array[chosen[0] + 1][chosen[1] - 1].getIsBomb():
                    array[chosen[0] + 1][chosen[1] - 1].incMinesAround()
            if chosen[0] + 1 < n:
                if not array[chosen[0] - 1][chosen[1]].getIsBomb():
                    array[chosen[0] - 1][chosen[1]].incMinesAround()
            if chosen[0] + 1 < n and chosen[1] + 1 < n:
                if not array[chosen[0] - 1][chosen[1] - 1].getIsBomb():
                    array[chosen[0] - 1][chosen[1] - 1].incMinesAround()
        #array[chosen[0]][chosen[1]].setMinesAround(5)

    return array
def printArrayState(array,n):
    for i in range(n):
        for j in range(n):
            print(array[i][j].getIsBomb(),end=" ")
        print()

def printMinesAround(array,n):
    for i in range(n):
        for j in range(n):
            print(array[i][j].getMinesAround(),end=" ")
        print()


array=isBombArray(5,5)
printArrayState(array,5)
printMinesAround(array,5)