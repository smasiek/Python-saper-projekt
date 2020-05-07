'''Importowane biblioteki'''
import random


class field:
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
    def getMines(self):
        return self._minesAround
    def getState(self):
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
    array=[[False for j in range(n)]for i in range(n)]
    possibilities=[[[i,j]for j in range(n)]for i in range(n)]

    for i in range(bombs):
        '''Uzupelnianie minami'''

        chosen = random.choice(random.choice(possibilities))
        array[chosen[0]][chosen[1]]=True
    return array
print (isBombArray(5,5))