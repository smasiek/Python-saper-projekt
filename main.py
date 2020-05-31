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
    def __init__(self,y,x,height,width,clicked,image):
        '''
        x,y - koordynaty pola
        height,width - wymiary pola
        clicked - 0-nie,1-LPM,2-PPMx1,3-PPMx2
        '''
        self._rect=pygame.rect.Rect(x,y+75,height,width)
        self._x = x
        self._y = y+75
        self._height = height
        self._width = width
        self._clicked = clicked
        self._image = image

    def getPxX(self):
        return int(self._x)

    def getPxY(self):
        return int(self._y) #75 = topBarHeight

    def draw(self,window):
        window.blit(self._image, (self.getPxX(),self.getPxY()))

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

    def getRect(self):
        return self._rect

    def getVisibleCount(self):
        return self.visibleCount

#Zainicjowanie zmiennych globalnych n i m oraz bombs
n=0
m=0
bombs=0

def configuration():
    screen = pygame.display.set_mode((600, 200))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box_n = pygame.Rect(25, 100, 100, 32)
    input_box_m = pygame.Rect(250, 100, 100, 32)
    input_box_bombs = pygame.Rect(475, 100, 50, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color_correct = pygame.Color('forestgreen')
    color_incorrect = pygame.Color('firebrick1')
    color_n = color_inactive
    color_m = color_inactive
    color_bombs = color_inactive
    active_n = False
    active_m = False
    active_bombs = False
    text_n = 'Podaj n'
    text_m = 'Podaj m'
    text_bombs = 'Bomby'
    input=[False,False,False]
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if input[0]==False or input[1]==False or input[2]==False:
                    pass
                else:
                    run = False
                #pygame.quit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if not input[0]:
                    if input_box_n.collidepoint(event.pos):
                        # Toggle the active variable.
                        text_n=''
                        active_n = not active_n
                    else:
                        active_n = False
                        if text_n=='':
                            text_n = 'Podaj n'

                    color_n = color_active if active_n else color_inactive

                if not input[1]:
                    if input_box_m.collidepoint(event.pos):
                        # Toggle the active variable.
                        text_m = ''
                        active_m = not active_m
                    else:
                        active_m = False
                        if text_m=='':
                            text_m = 'Podaj m'
                    # Change the current color of the input box.
                    color_m = color_active if active_m else color_inactive

                if not input[2]:
                    if input_box_bombs.collidepoint(event.pos):
                        # Toggle the active variable.
                        text_bombs = ''
                        active_bombs = not active_bombs
                    else:
                        active_bombs = False
                        if text_bombs=='':
                            text_bombs = 'Bomby'
                    # Change the current color of the input box.
                    color_bombs = color_active if active_bombs else color_inactive


            if event.type == pygame.KEYDOWN:
                if active_n:
                    if event.key == pygame.K_RETURN:

                        if 2<=int(text_n)<=15:
                            global n
                            color_n=color_correct
                            input[0]=True
                            print(text_n)
                            n=int(text_n)
                            text_n = ''
                            active_n = not active_n
                        else:
                            color_n = color_incorrect
                            #Rzuca wyjątek - zle dane


                    elif event.key == pygame.K_BACKSPACE:
                        text_n = text_n[:-1]
                    else:
                        text_n += event.unicode
                if active_m:
                    if event.key == pygame.K_RETURN:
                        if 2 <= int(text_m) <= 15:
                            global m
                            color_m = color_correct
                            input[1] = True
                            print(text_m)
                            m = int(text_m)
                            text_m = ''
                            active_m = not active_m
                        else:
                            color_m = color_incorrect
                            # Rzuca wyjątek - zle dane
                    elif event.key == pygame.K_BACKSPACE:
                        text_m = text_m[:-1]
                    else:
                        text_m += event.unicode

                if active_bombs:
                    if event.key == pygame.K_RETURN:
                        if 0 <= int(text_bombs) <= n*m:
                            global bombs
                            color_bombs = color_correct
                            input[2] = True
                            print(text_bombs)
                            bombs = int(text_bombs)
                            text_bombs = ''
                            active_bombs = not active_bombs
                        else:
                            color_bombs = color_incorrect
                            # Rzuca wyjątek - zle dane
                    elif event.key == pygame.K_BACKSPACE:
                        text_bombs = text_bombs[:-1]
                    else:
                        text_bombs += event.unicode



            screen.fill((255, 255, 255))
            # Render the current text.
            txt_surface_n = font.render(text_n, True, color_n)
            txt_surface_m = font.render(text_m, True, color_m)
            txt_surface_bombs = font.render(text_bombs, True, color_bombs)
            # Resize the box if the text is too long.
            width_n = max(200, txt_surface_n.get_width() + 10)
            width_m = max(200, txt_surface_m.get_width() + 10)
            width_bombs = max(50, txt_surface_bombs.get_width() + 10)
            input_box_n.w = width_n
            input_box_m.w = width_m
            input_box_bombs.w = width_bombs
            # Blit the text.
            screen.blit(txt_surface_n, (input_box_n.x + 5, input_box_n.y + 5))
            screen.blit(txt_surface_m, (input_box_m.x + 5, input_box_m.y + 5))
            screen.blit(txt_surface_bombs, (input_box_bombs.x + 5, input_box_bombs.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color_n, input_box_n, 2)
            pygame.draw.rect(screen, color_m, input_box_m, 2)
            pygame.draw.rect(screen, color_bombs, input_box_bombs, 2)

            pygame.display.flip()
            clock.tick(30)

configuration()
'''Tu zrobic funkcje ktora w okienku bedzie obslugiwala wpisywanie n i m a potem tworzenie okna, poki co z ręki:'''
#n=4
#m=9
#bombs=15

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

def checkIfWin(squares,fields,x,y):
    if (m*n)-squares[x][y].visibleCount<=bombs:
        print('win')
        return endGame(squares, fields)
    if Field.flaggedBombCount==bombs and Square.flaggedCount == bombs:
        print('win')
        return endGame(squares, fields)
'''koniec metod klasy plansza'''


def reveal(squares,fields,x,y):
    if squares[x][y].getClicked() == 0:
        if fields[x][y].isBomb():
            squares[x][y].setImage(bomb)
            squares[x][y].draw(screen)
            squares[x][y].setClicked(1)
            endGame(squares, fields)
            pygame.display.update()
        else:
            squares[x][y].setImage(numbers[fields[x][y].getMinesAround()])
            squares[x][y].draw(screen)
            #squares[i][j].incVisibleCount()
            squares[x][y].setClicked(1)
            if fields[x][y].getMinesAround() == 0:
                flood(squares, fields, numbers, screen, x, y, n, m)
            checkIfWin(squares, fields, x, y)
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
        for j in range(m):
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



#n=4 m=9
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
                #isBreak=False
                for i in range(n):
                    for j in range(m):
                        r=pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
                        if squares[i][j].getRect().colliderect(r):
                            reveal(squares,fields,i,j)
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

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        r = pygame.rect.Rect(pygame.mouse.get_pos(), (1, 1))
                        if squares[i][j]._rect.colliderect(r):
                            if squares[i][j].getClicked() == 0:
                                fields[i][j].incBombFlagged()
                                squares[i][j].setImage(flag)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(2)
                                checkIfWin(squares, fields, i, j)
                                pygame.display.update()

                            elif squares[i][j].getClicked() == 2:
                                fields[i][j].decBombFlagged()
                                squares[i][j].setImage(qmark)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(3)
                                pygame.display.update()
                            elif squares[i][j].getClicked() == 3:
                                squares[i][j].setImage(default)
                                squares[i][j].draw(screen)
                                squares[i][j].setClicked(0)
                                checkIfWin(squares, fields, i, j)
                                pygame.display.update()
                    else:
                           pass#print(squares[i][j]._rect)
                                            #print(squares[i][j].getClicked())
                                #pygame.display.update()





minesweeper(n,m,bombs)