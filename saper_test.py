import unittest
import pygame
import logic.fields as fd
import graphics.icons as ic
import graphics.windows as wd
import graphics.squares as sq

class TestSum(unittest.TestCase):


    def test_one(self):
        text_n="1"
        text_m="1"
        text_bombs="1"
        with self.assertRaises(wd.ZleWymiaryException):
            if 2 <= int(text_n) <= 15:
                n = int(text_n)
            else:
                raise wd.ZleWymiaryException(text_n)

        text_n = "5"
        text_m = "1"
        text_bombs = "2"
        with self.assertRaises(wd.ZleWymiaryException):
            if 2 <= int(text_m) <= 15:
                n = int(text_m)
            else:
                raise wd.ZleWymiaryException(text_m)

        text_n = "4"
        text_m = "1"
        text_bombs = "2"
        with self.assertRaises(wd.ZleWymiaryException):
            if 2 <= int(text_m) <= 15:
                n = int(text_m)
            else:
                raise wd.ZleWymiaryException(text_m)

        text_n = "20"
        text_m = "500"
        text_bombs = "12"
        with self.assertRaises(wd.ZleWymiaryException):
            if 2 <= int(text_n) <= 15:
                n = int(text_n)
            else:
                raise wd.ZleWymiaryException(text_n)

        text_n = "5"
        text_m = "6"
        text_bombs = "-4"
        with self.assertRaises(wd.BombsException):
            n=int(text_n)
            m=int(text_m)
            if 0 <= int(text_bombs) <= n * m:
                pass
            else:
                raise wd.BombsException(text_bombs)

        text_n = "3"
        text_m = "3"
        text_bombs = "10"
        with self.assertRaises(wd.BombsException):
            n = int(text_n)
            m = int(text_m)
            if 0 <= int(text_bombs) <= n * m:
                pass
            else:
                raise wd.BombsException(text_bombs)

        text_n = "1"
        text_m = "10"
        text_bombs = "5"
        with self.assertRaises(wd.ZleWymiaryException):
            if 2 <= int(text_n) <= 15:
                n = int(text_n)
            else:
                raise wd.ZleWymiaryException(text_n)

    def test_two(self):
        miny=0
        square=sq.Square(0-75,0,60,60,0,ic.default) #-75 ze wzgledu na topbar
        field=fd.Field(False,1,1,5) #przechowuje informacje o bombach
        r = pygame.rect.Rect((5,5), (1, 1))# (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        if square.getRect().colliderect(r):
            miny=field.getMinesAround()
        self.assertEqual(5,miny)

    def test_three(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        field = fd.Field(True, 1, 1, 5) #przechowuje informacje o bombach
        r = pygame.rect.Rect((5, 5), (1, 1)) # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        if square.getRect().colliderect(r):
            if field.isBomb():
                square.setImage(ic.bomb)
                endGame=True
        self.assertTrue(endGame)
        self.assertEqual(ic.bomb,square._image)

    def test_four(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        field = fd.Field(False, 0, 0, 0) #przechowuje informacje o bombach

        r = pygame.rect.Rect((5, 5), (1, 1)) # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        if square.getRect().colliderect(r):
            reveal=True #funkcja wywolujaca sprawdzenie, uruchomienie wymagałoby utworzenia nowego okna gry
        self.assertTrue(reveal)
        self.assertEqual(0,field.getMinesAround())

    def test_five(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        sq.Square.flaggedCount=0
        r = pygame.rect.Rect((5, 5), (1, 1)) # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        if square.getRect().colliderect(r):
            square.setClicked(2) #tu jest mina - oflagowanie
        self.assertEqual(2,square.getClicked())
        self.assertEqual(1,sq.Square.flaggedCount)

    def test_six(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        sq.Square.flaggedCount=0
        r = pygame.rect.Rect((5, 5), (1, 1)) # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        '''Symulacja klikniec w przycisk'''
        if square.getRect().colliderect(r):
            square.setClicked(2) #tu jest mina - oflagowanie
        if square.getRect().colliderect(r):
            square.setClicked(3) #tu moze byc mina - pytajnik
        self.assertEqual(3,square.getClicked())
        self.assertEqual(0,sq.Square.flaggedCount)

    def test_seven(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        sq.Square.flaggedCount = 0

        r = pygame.rect.Rect((5, 5), (1, 1))  # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie

        """
        Symulacja kliknięć na pole: tu jest mina,tu moze byc mina,odznacz
        """
        if square.getRect().colliderect(r):
            square.setClicked(2)
        self.assertEqual(2,square.getClicked())
        self.assertEqual(1,sq.Square.flaggedCount)

        if square.getRect().colliderect(r):
            square.setClicked(3)
        self.assertEqual(3, square.getClicked())
        self.assertEqual(0, sq.Square.flaggedCount)

        if square.getRect().colliderect(r):
            square.setClicked(0)
        self.assertEqual(0, square.getClicked())
        self.assertEqual(0, sq.Square.flaggedCount)

        """
        Druga symulacja kliknięć na pole: tu jest mina,tu moze byc mina,odznacz
        """
        if square.getRect().colliderect(r):
            square.setClicked(2)
        self.assertEqual(2, square.getClicked())
        self.assertEqual(1, sq.Square.flaggedCount)

        if square.getRect().colliderect(r):
            square.setClicked(3)
        self.assertEqual(3, square.getClicked())
        self.assertEqual(0, sq.Square.flaggedCount)

        if square.getRect().colliderect(r):
            square.setClicked(0)
        self.assertEqual(0, square.getClicked())
        self.assertEqual(0, sq.Square.flaggedCount)

    def test_eight(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        square1 = sq.Square(0 - 75, 60, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        win=False

        r = pygame.rect.Rect((5, 5), (1, 1)) # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie

        '''Symulacja klikniec w recznie stworzone pola'''
        if square.getRect().colliderect(r):
            square.setClicked(1)
        r1 = pygame.rect.Rect((65, 5), (1, 1))  # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        if square1.getRect().colliderect(r1):
            square1.setClicked(1)

        '''Fragment funkcji sprawdzającej wygraną - sprawdzający kliknięcia'''
        if 2 - sq.Square.visibleCount <= 0:
            win=True
        self.assertTrue(win)

    def test_nine(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        square1 = sq.Square(0 - 75, 60, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar
        sq.Square.flaggedCount=0
        bombs = 2
        win=False
        '''field przechowuje informacje o byciu bombą poszczegolnych kwadratow'''
        field = fd.Field(True, 0, 0, 1)
        field1 = fd.Field(True, 0, 1, 1)

        '''Symulacja klikniec w recznie stworzone pola'''
        r = pygame.rect.Rect((5, 5), (1, 1)) # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        if square.getRect().colliderect(r):
            square.setClicked(2)
            field.incBombFlagged()
        r1 = pygame.rect.Rect((65, 5), (1, 1))  # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        if square1.getRect().colliderect(r1):
            square.setClicked(2)
            field1.incBombFlagged()

        '''Fragment funkcji sprawdzającej wygraną - sprawdzający oflagowanie'''
        if fd.Field.flaggedBombCount == bombs and sq.Square.flaggedCount == bombs:
            win=True

        self.assertTrue(win)

    def test_ten(self):
        square = sq.Square(0 - 75, 0, 60, 60, 0, ic.default)  # -75 ze wzgledu na topbar

        r = pygame.rect.Rect((5, 5), (1, 1)) # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie

        '''Symulacja kliknięcia w przycisk'''
        if square.getRect().colliderect(r):
            square.setClicked(1)
        self.assertEqual(1,square.getClicked())
        self.assertEqual(0,sq.Square.flaggedCount)

        '''Symulacja flagowania klikniętego przycisku'''
        if square.getRect().colliderect(r):
            square.setClicked(2)
        self.assertNotEqual(2, square.getClicked())
        self.assertNotEqual(1, sq.Square.flaggedCount)

    def test_eleven(self):
        '''
        By odpowiednio wykonać ten test musialbym stworzyc nowe okno gry ale w __init__ okna gry wystepuje pole z "kotkiem"
        symbolizującym wygraną lub przegraną ktory nie jest zdefiniowany w pliku testów tak samo jak timer.
        Z tego powodu będe testować jedynie wybrane linie kodu, które działają tak samo jak w oficjalnym programie
        '''
        n=5
        m=5
        topBarHeight=75
        squareHeight=60
        squareWidth=60
        sq.Square.flaggedCount=0
        squares = [[sq.Square(i * squareHeight-topBarHeight, j * squareWidth, squareHeight, squareWidth, 0, ic.default)for j in range(m)] for i in range(n)]

        r = pygame.rect.Rect((5, 5), (1, 1))  # (5, 5) to koordy - oryginalnie get_pos, (1, 1) to wymiary kwadracika ktory reprezentuja kliknięcie
        '''Symulacja klikniec'''
        if squares[0][0].getRect().colliderect(r):
            squares[0][0].setClicked(1)
        self.assertEqual(1, squares[0][0].getClicked())
        self.assertEqual(0, sq.Square.flaggedCount)

        r = pygame.rect.Rect((65, 5), (1, 1))
        if squares[0][1].getRect().colliderect(r):
            squares[0][1].setClicked(1)
        self.assertEqual(1, squares[0][1].getClicked())
        self.assertEqual(0, sq.Square.flaggedCount)
        '''Symulacja oflagowania'''
        r = pygame.rect.Rect((125, 5), (1, 1))
        if squares[0][2].getRect().colliderect(r):
            squares[0][2].setClicked(2)
        self.assertEqual(2, squares[0][2].getClicked())
        self.assertEqual(1, sq.Square.flaggedCount)

        '''
        reset pól, jest, to po prostu przygotowanie od nowa planszy, w ten sam sposob odbywa się to w programie
        z zaznaczeniem, że w programie generuje się od razu nowa plansza, z losowo rozmieszczonymi bombami w innych miejscach
        w tym tescie nie tworze tablicy fields ukazującej rozmieszczenie bomb
        '''
        squares = [[sq.Square(i * squareHeight - topBarHeight, j * squareWidth, squareHeight, squareWidth, 0, ic.default) for j in
                    range(m)] for i in range(n)]
        sq.Square.visibleCount = 0
        sq.Square.flaggedCount = 0

        self.assertEqual(0, squares[0][0].getClicked())
        self.assertEqual(0, squares[0][1].getClicked())
        self.assertEqual(0, squares[0][2].getClicked())
        self.assertEqual(0, sq.Square.flaggedCount)

    def test_twelve(self):
        xyzzySequence = [False, False, False, False, False]
        n = 5
        m = 5
        topBarHeight = 75
        squareHeight = 60
        squareWidth = 60
        sq.Square.flaggedCount = 0
        squares = [[sq.Square(i * squareHeight - topBarHeight, j * squareWidth, squareHeight, squareWidth, 0, ic.default) for j in
                    range(m)] for i in range(n)]

        '''Symulacja klikniec przyciskow w odpowiedniej kolejnosci(xyzzy)'''
        x=pygame.K_x
        y=pygame.K_y
        z=pygame.K_z
        if x==pygame.K_x:
            xyzzySequence[0] = True
        if y==pygame.K_y and xyzzySequence[0] == True:
            xyzzySequence[0] = False
            xyzzySequence[1] = True
        if z==pygame.K_z and xyzzySequence[1] == True:
            xyzzySequence[1] = False
            xyzzySequence[2] = True
        if z==pygame.K_z and xyzzySequence[2] == True:
            xyzzySequence[2] = False
            xyzzySequence[3] = True
        if y==pygame.K_y and xyzzySequence[3] == True:
            xyzzySequence[3] = False
            xyzzySequence[4] = True
            #wywolanie funkcji xyzzy
            #gameWindow.xyzzy(fields)

            #w tescie ręcznie zmienie grafiki pól
            squares[0][0].setImage(ic.xyzz)
            squares[1][1].setImage(ic.xyzz)

        self.assertEqual(ic.xyzz, squares[0][0]._image)
        self.assertEqual(ic.xyzz, squares[1][1]._image)

        '''Funkcja resetująca plansze, uzasadnienie podobnie jak w test_eleven'''
        squares = [[sq.Square(i * squareHeight - 75, j * squareWidth, squareHeight, squareWidth, 0, ic.default) for j in
                    range(m)] for i in range(n)]
        sq.Square.visibleCount = 0
        sq.Square.flaggedCount = 0

        self.assertNotEqual(ic.xyzz, squares[0][0]._image)
        self.assertNotEqual(ic.xyzz, squares[1][1]._image)

if __name__ == '__main__':
    unittest.main()