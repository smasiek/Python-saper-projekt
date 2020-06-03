import pygame
import graphics.squares as sq
import graphics.icons as ic
import logic.fields as fd
pygame.init()

class GameWindow:
    def __init__(self,n,m,topBarHeight):
        '''LAMBDA #x'''
        self.squareHeight = (lambda n,m:100 if  n < 8 and m < 8 else 60)(n,m)
        self.squareWidth = (lambda n,m:100 if  n < 8 and m < 8 else 60)(n,m)
        self.topBar = topBarHeight
        '''LAMBDA #y'''
        self.height=(lambda n1,m1: 100*n1+topBarHeight if  n1 < 8 and m1 < 8 else 60*n1+topBarHeight)(n,m)
        self.width=(lambda n1,m1:100*m1 if  n1 < 8 and m1 < 8 else 60*m1)(n,m)
        self.window=pygame.display
        self.screen=pygame.display
        '''LIST COMPREHENSIONS #3'''
        self.squares=[[sq.Square(i*self.squareHeight,j*self.squareWidth,self.squareHeight,self.squareWidth,0,ic.default)for j in range(m)]for i in range(n)]

    def resetSquares(self):
        n = len(self.squares)
        m = len(self.squares[0])
        self.squares = [[sq.Square(i * self.squareHeight, j * self.squareWidth, self.squareHeight, self.squareWidth, 0, ic.default)for j in range(m)] for i in range(n)]

    def endGame(self,fields):
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                if self.squares[i][j].getClicked() == 0 or self.squares[i][j].getClicked() == 2 or self.squares[i][
                    j].getClicked() == 3:
                    if fields[i][j].isBomb():
                        self.squares[i][j].setImage(ic.bomb)
                        self.squares[i][j].draw(self.screen)
                        self.squares[i][j].setClicked(1)
                    else:
                        self.squares[i][j].setImage(ic.numbers[fields[i][j].getMinesAround()])
                        self.squares[i][j].draw(self.screen)
                        self.squares[i][j].setClicked(1)
        pygame.display.update()

    def checkIfWin(self, fields, x, y,bombs):
        n=len(self.squares)
        m=len(self.squares[0])
        if (m * n) - self.squares[x][y].visibleCount <= bombs:
            print('win')
            return self.endGame(fields)
        if fd.Field.flaggedBombCount == bombs and sq.Square.flaggedCount == bombs:
            print('win')
            return self.endGame(fields)

    def reveal(self, fields, x, y,bombs):
        if self.squares[x][y].getClicked() == 0:
            if fields[x][y].isBomb():
                self.squares[x][y].setImage(ic.bomb)
                self.squares[x][y].draw(self.screen)
                self.squares[x][y].setClicked(1)
                self.endGame(fields)
                pygame.display.update()
            else:
                self.squares[x][y].setImage(ic.numbers[fields[x][y].getMinesAround()])
                self.squares[x][y].draw(self.screen)
                # squares[i][j].incVisibleCount()
                self.squares[x][y].setClicked(1)
                if fields[x][y].getMinesAround() == 0:
                    self.flood(fields, x, y, bombs)
                self.checkIfWin(fields, x, y, bombs)
                pygame.display.update()

    def flood(self, fields, i, j,bombs):
        n = len(self.squares)
        m = len(self.squares[0])
        tab = [-1, 0, 1]
        for l in tab:
            for k in tab:
                ii = i + l
                jj = j + k
                if ii > -1 and ii < n and jj > -1 and jj < m:
                    if not fields[ii][jj].isBomb():
                        self.reveal(fields, ii, jj, bombs)

    def xyzzy(self, fields):
        n = len(self.squares)
        m = len(self.squares[0])
        for i in range(n):
            for j in range(m):
                if fields[i][j].isBomb():
                    if not self.squares[i][j].getClicked() == 2:
                        self.squares[i][j].setImage(ic.xyzz)
                        self.squares[i][j].draw(self.screen)
                    else:
                        self.squares[i][j].setImage(ic.flaggedxyzz)
                        self.squares[i][j].draw(self.screen)
        pygame.display.update()

    def drawScene(self):

        for i in range(len(self.squares)):
            for j in range(len(self.squares[i])):
                self.squares[i][j].draw(self.window)

    def clearWindow(self):
        self.window.fill((255, 255, 255))

    def setWindow(self):
        print("USTAWIONE WYMIARY: wd: ",self.width," hg: ",self.height)
        self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.window.fill((255, 255, 255))

    def setScreen(self):
        self.screen = pygame.display.get_surface()

    def getWindow(self):
        return self.window

    def getScreen(self):
        return self.screen

    def getSquareH(self):
        return self.squareHeight

    def getSquareW(self):
        return self.squareWidth

    def getSquares(self):
        return self.squares



def configuration():
    height=180
    width=600
    res=(width, height)
    screen = pygame.display.set_mode(res)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box_n = pygame.Rect(50, 25, 100, 32)
    input_box_m = pygame.Rect(50, 75, 100, 32)
    input_box_bombs = pygame.Rect(105, 125, 50, 32)
    ok = pygame.image.load("icons\\acceptIn.png")
    ok.convert()
    rectOk = ok.get_rect()
    rectOk.center = (425, 90)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color_correct = pygame.Color('forestgreen')
    color_incorrect = pygame.Color('firebrick1')
    color_n = color_inactive
    color_m = color_inactive
    color_bombs = color_incorrect
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
            '''LAMBDA #1'''
            if (lambda ev: event.type == ev)(pygame.QUIT):
                run = False
                pygame.quit()

            '''LAMBDA #2'''

            if (lambda ev: event.type == ev)(pygame.MOUSEBUTTONDOWN):
                # If the user clicked on the input_box rect.
                if rectOk.collidepoint(event.pos):
                    if input[0] and input[1] and input[2]:
                        run = False
                        return n, m, bombs
                if not input[0]:
                    #if input_box_n.collidepoint(event.pos):
                    if input_box_n.collidepoint(event.pos):
                        # Toggle the active variable.
                        text_n=''
                        active_n = not active_n
                    else:
                        active_n = False
                        if text_n=='':
                            text_n = 'Podaj n'

                    if active_n:
                        color_n = color_active
                    else:
                        color_n = color_inactive
                        text_n = 'Podaj n'

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
                    if active_m:
                        color_m = color_active
                    else:
                        color_m = color_inactive
                        text_m = 'Podaj m'

                if input[0] and input[1]:
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

            '''LAMBDA #3'''
            if (lambda ev: event.type == ev)(pygame.KEYDOWN):
                if active_n:
                    if event.key == pygame.K_RETURN:
                        if 2<=int(text_n)<=15:
                            color_n=color_correct
                            input[0]=True
                            print(text_n)
                            n=int(text_n)
                            active_n = not active_n
                            if not input[1]:
                                active_n = False
                                active_m = True
                                text_m = ''
                                color_m = color_active
                                pygame.display.flip()
                                break
                        else:
                            color_n = color_incorrect
                            #Rzuca wyjątek - zle dane
                        if input[0] and input[1]:
                            color_bombs = color_inactive
                    elif event.key == pygame.K_BACKSPACE:
                        text_n = text_n[:-1]
                    elif event.key == pygame.K_TAB:
                        if not input[1]:
                            active_n = False
                            color_n = color_inactive
                            active_m = True
                            text_m = ''
                            text_n = 'Podaj n'
                            color_m = color_active
                            pygame.display.flip()
                            break
                    else:
                        text_n += event.unicode

                if active_m:
                    if event.key == pygame.K_RETURN:
                        if 2 <= int(text_m) <= 15:
                            color_m = color_correct
                            input[1] = True
                            print(text_m)
                            m = int(text_m)
                            active_m = not active_m
                            if input[0]:
                                active_m = False
                                active_bombs = True
                                text_bombs = ''
                                color_bombs = color_active
                                pygame.display.flip()
                                break
                        else:
                            color_m = color_incorrect
                            # Rzuca wyjątek - zle dane
                        if input[0] and input[1]:
                            color_bombs = color_inactive
                    elif event.key == pygame.K_BACKSPACE:
                        text_m = text_m[:-1]
                    elif event.key == pygame.K_TAB:
                        if not input[0]:
                            active_m=False
                            color_m = color_inactive
                            active_n=True
                            text_n = ''
                            text_m = 'Podaj m'
                            color_n = color_active
                            pygame.display.flip()
                    else:
                        text_m += event.unicode

                if active_bombs:
                    if input[0] and input[1]:
                        if event.key == pygame.K_RETURN:
                            if 0 <= int(text_bombs) <= n*m:
                                #global bombs
                                color_bombs = color_correct
                                input[2] = True
                                print(text_bombs)
                                bombs = int(text_bombs)
                                #text_bombs = ''
                                active_bombs = not active_bombs
                            else:
                                color_bombs = color_incorrect
                                # Rzuca wyjątek - zle dane
                            if input[0] and input[1] and input[2]:
                                ok = pygame.image.load("icons\\accept.png")
                        elif event.key == pygame.K_BACKSPACE:
                            text_bombs = text_bombs[:-1]
                        else:
                            text_bombs += event.unicode
                #if event.key == pygame.K_RETURN:
                 #   if input[0] == True and input[1] and True and input[2] == True:
                 #       run = False
                 #       return n, m, bombs


            screen.fill((255, 255, 255))
            #ok_button=sq.Square(y, x, height, width, clicked, image)
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
            screen.blit(ok, rectOk)
            # Blit the input_box rect.
            pygame.draw.rect(screen, color_n, input_box_n, 2)
            pygame.draw.rect(screen, color_m, input_box_m, 2)
            pygame.draw.rect(screen, color_bombs, input_box_bombs, 2)

            pygame.display.flip()
            clock.tick(30)



