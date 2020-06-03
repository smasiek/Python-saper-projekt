import random

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


def getMatrix(n,m,bombs):
    '''
    :param n: 1st wymiar planszy
    :param m: 2nd wymiar planszy
    :param bombs: ilosc bomb
    :return: plansza true/false
    '''
    '''LIST COMPREHENSIONS #1 i #2'''
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