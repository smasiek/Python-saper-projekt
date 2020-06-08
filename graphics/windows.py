"""Module handling GUI"""
import pygame

import logic.fields as fd
import graphics.icons as ic
import graphics.icons_big as ic_b
import graphics.squares as sq

# import graphics.icons as ic
pygame.init()


class Error(Exception):
    """Abstract class to be inherited by other exception classes."""


class ZleWymiaryException(Error):
    """Throw exception when size of game window is invalid."""

    def __init__(self, data):
        self._input = data

    def __str__(self):
        return "Podano zle wymiary: {0}. Oczekiwano: 1 < n,m < 16".format(self._input)


class NullInputException(Error):
    """Throw exception when there's no input."""

    def __str__(self):
        return "Nie podano inputu. Oczekiwano cyfry"


class InvalidInputException(Error):
    """Throw exception when size of game window contains letters."""

    def __init__(self, data):
        self._input = data

    def __str__(self):
        return "Podano zly input: {0}. Oczekiwano cyfry".format(self._input)


class BombsException(Error):
    """Throw exception when number of bombs is invalid."""

    def __init__(self, data):
        self._input = data

    def __str__(self):
        return "Podano zla ilosc bomb: {0}. Oczekiwano: 0 < bombs <= n*m".format(self._input)


class Timer:
    """Represent timer."""

    def __init__(self, start, time, x, y):
        self._x = x
        self._y = y
        self._start = start
        self._time = str(time)
        self._timeWindow = pygame.Rect(25, 25, 50, 32)
        self._font = pygame.font.Font(None, 32)
        self._color = pygame.Color('dodgerblue2')

    def set_time(self, start, time, screen):
        """Set timer's initial values and blit timer"""
        self._start = start
        self._time = str(time)
        txt_surface = self._font.render(self._time, True, self._color)
        screen.blit(txt_surface, (self._timeWindow.x + 5, self._timeWindow.y + 5))
        pygame.draw.rect(screen, self._color, self._timeWindow, 2)
        pygame.display.flip()

    def update_time(self, time, screen):
        """Update timer values and blit it"""
        self._time = str(time)
        txt_surface = self._font.render(self._time, True, self._color)
        screen.blit(txt_surface, (self._timeWindow.x + 5, self._timeWindow.y + 5))
        pygame.draw.rect(screen, self._color, self._timeWindow, 2)
        pygame.display.flip()

    def draw_timer(self, screen):
        """Blit timer with it's values"""
        txt_surface = self._font.render(self._time, True, self._color)
        screen.blit(txt_surface, (self._timeWindow.x + 5, self._timeWindow.y + 5))
        pygame.draw.rect(screen, self._color, self._timeWindow, 2)

    def get_time(self):
        """Return timer"""
        return self._time


class Cat:
    """Represent cat icon on game window."""

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._width = 60
        self._height = 60
        self._img = self._rect = pygame.rect.Rect(self._x, self._y, self._height, self._width)

    def set_cat(self, screen, icon):
        """Blit present cat icon"""
        screen.blit(icon, (self._x, self._y))

    def get_cat(self):
        """Return cat's image"""
        return self._img


class GameWindow:
    """Represent game window."""

    def __init__(self, n, m, top_bar_height):
        """LAMBDA #x"""
        self.square_height = (lambda n1, m1: 100 if n1 < 8 and m1 < 8 else 60)(n, m)
        self.square_width = (lambda n1, m1: 100 if n1 < 8 and m1 < 8 else 60)(n, m)
        self.top_bar = top_bar_height
        self.height = self.square_height * n + self.top_bar
        self.width = self.square_width * m
        self.window = pygame.display
        self.screen = pygame.display
        self._timer = Timer(0, 0, 5, 5)
        self._cat = Cat(self.width // 2.2, 15)
        self._started = False

        # Set icon depending on size of square.
        if self.square_height > 60:
            self.squares = [[sq.Square(i * self.square_height, j * self.square_width,
                                       self.square_height, self.square_width,
                                       0, ic_b.default) for j in range(m)] for i in range(n)]
        else:
            self.squares = [[sq.Square(i * self.square_height, j * self.square_width,
                                       self.square_height, self.square_width,
                                       0, ic.default) for j in range(m)] for i in range(n)]

    def reset_squares(self):
        """Reset array of fields.

        All it does is overwriting current array with new default squares.
        """
        n = len(self.squares)
        m = len(self.squares[0])
        if self.square_height > 60:
            self.squares = [[sq.Square(i * self.square_height, j * self.square_width,
                                       self.square_height, self.square_width,
                                       0, ic_b.default) for j in range(m)] for i in range(n)]
        else:
            self.squares = [[sq.Square(i * self.square_height, j * self.square_width,
                                       self.square_height, self.square_width,
                                       0, ic.default) for j in range(m)] for i in range(n)]

    def end_game(self, fields):
        """End game by clicking every unclicked square"""
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                if self.squares[i][j].get_clicked() == 0 or\
                        self.squares[i][j].get_clicked() == 2 or\
                        self.squares[i][j].get_clicked() == 3:
                    if fields[i][j].is_bomb():
                        if self.squares[i][j].get_size() > 60:
                            self.squares[i][j].set_image(ic_b.bomb)
                        else:
                            self.squares[i][j].set_image(ic.bomb)
                        self.squares[i][j].draw(self.screen)
                        self.squares[i][j].set_clicked(1)

                    else:
                        if self.squares[i][j].get_size() > 60:
                            self.squares[i][j].set_image(
                                ic_b.numbers[fields[i][j].get_mines_around()])
                        else:
                            self.squares[i][j].set_image(
                                ic.numbers[fields[i][j].get_mines_around()])

                        self.squares[i][j].draw(self.screen)

                        self.squares[i][j].set_clicked(1)
        # Update flagged count and mark game as finished.
        self.squares[0][0].reset_flagged_count()
        self._started = False
        pygame.display.update()

    def check_if_win(self, fields, x, y, bombs):
        """Check if game is won."""
        n = len(self.squares)
        m = len(self.squares[0])
        # Win by clicking all free squares.
        if (m * n) - self.squares[x][y].visible_count <= bombs:
            print('win')
            self._cat.set_cat(self.screen, ic.catWin)
            return self.end_game(fields)
        # Win by flagging squares with bomb.
        if fd.Field.flagged_bomb_count == bombs and sq.Square.flagged_count == bombs:
            print('win')
            self._cat.set_cat(self.screen, ic.catWin)
            return self.end_game(fields)

    def reveal(self, fields, x, y, bombs):
        """Handle revealing clicked field."""
        if self.squares[x][y].get_clicked() == 0:
            # Check if square is bomb.
            if fields[x][y].is_bomb():
                print("lose")
                self._cat.set_cat(self.screen, ic.catLose)
                if self.squares[x][y].get_size() > 60:
                    self.squares[x][y].set_image(ic_b.bomb)
                else:
                    self.squares[x][y].set_image(ic.bomb)
                self.squares[x][y].draw(self.screen)
                self.squares[x][y].set_clicked(1)
                self.end_game(fields)
                pygame.display.update()
            else:
                # Reveal square without bomb.
                if self.squares[x][y].get_size() > 60:
                    self.squares[x][y].set_image(ic_b.numbers[fields[x][y].get_mines_around()])
                else:
                    self.squares[x][y].set_image(ic.numbers[fields[x][y].get_mines_around()])

                self.squares[x][y].draw(self.screen)
                self.squares[x][y].visible_count += 1
                self.squares[x][y].set_clicked(1)
                # If square has no bombs around run flood().
                if fields[x][y].get_mines_around() == 0:
                    self.flood(fields, x, y, bombs)
                self.check_if_win(fields, x, y, bombs)
                pygame.display.update()

    def flood(self, fields, i, j, bombs):
        """Function calling reveal() on neighbouring fields with no bombs around."""
        n = len(self.squares)
        m = len(self.squares[0])
        tab = [-1, 0, 1]
        for l in tab:
            for k in tab:
                ii = i + l
                jj = j + k
                if n > ii > -1 < jj < m:
                    if not fields[ii][jj].is_bomb():
                        self.reveal(fields, ii, jj, bombs)

    def xyzzy(self, fields):
        """Handle cheat sequence.

        Set icon of squares with bomb to cheated one.
        """
        n = len(self.squares)
        m = len(self.squares[0])
        for i in range(n):
            for j in range(m):
                if fields[i][j].is_bomb():
                    if not self.squares[i][j].get_clicked() == 2:
                        if self.squares[i][j].get_size() > 60:
                            self.squares[i][j].set_image(ic_b.xyzz)
                        else:
                            self.squares[i][j].set_image(ic.xyzz)
                        self.squares[i][j].draw(self.screen)
                    else:
                        if self.squares[i][j].get_size() > 60:
                            self.squares[i][j].set_image(ic_b.flaggedxyzz)
                        else:
                            self.squares[i][j].set_image(ic.flaggedxyzz)
                        self.squares[i][j].draw(self.screen)
        pygame.display.flip()

    def draw_scene(self):
        """Blit initial state of game."""
        for i in range(len(self.squares)):
            for j in range(len(self.squares[i])):
                self.squares[i][j].draw(self.window)
        self._cat.set_cat(self.screen, ic.cat)
        self._timer.draw_timer(self.screen)

    def clear_window(self):
        """Wipe off everything of the screen."""
        self.window.fill((255, 255, 255))

    def set_window(self):
        """Set window resolution."""
        print("USTAWIONE WYMIARY: wd: ", self.width, " hg: ", self.height)
        self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.window.fill((255, 255, 255))

    def set_screen(self):
        """Set screen and timer."""
        self.screen = pygame.display.get_surface()
        self._timer.set_time(0, 0, self.screen)

    def set_started(self):
        """Set game as started."""
        self._started = True

    def reset_started(self):
        """Set game as finished."""
        self._started = False

    def get_window(self):
        """Return window object."""
        return self.window

    def get_screen(self):
        """Return screen object."""
        return self.screen

    def get_timer(self):
        """Return timer of current game."""
        return self._timer

    def get_square_h(self):
        """Return height of a single square."""
        return self.square_height

    def get_square_w(self):
        """Return width of a single square."""
        return self.square_width

    def get_squares(self):
        """Return matrix of squares from current game."""
        return self.squares

    def get_cat(self):
        """Return cat object from current game"""
        return self._cat

    def get_started(self):
        """Return True if game is started"""
        return self._started


def configuration():
    """Window set to configure game window."""
    pygame.display.set_caption("Konfiguracja sapera")
    pygame.display.set_icon(ic.icon)
    height = 180
    width = 600
    res = (width, height)
    screen = pygame.display.set_mode(res)
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box_n = pygame.Rect(50, 25, 100, 32)
    input_box_m = pygame.Rect(50, 75, 100, 32)
    input_box_bombs = pygame.Rect(105, 125, 50, 32)
    ok = pygame.image.load("icons\\acceptIn.png")
    ok.convert()
    rect_ok = ok.get_rect()
    rect_ok.center = (425, 90)
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
    inputs = [False, False, False]  # Used to control input boxes.
    run = True

    while run:
        for event in pygame.event.get():
            if (lambda ev: event.type == ev)(pygame.QUIT):
                run = False
                pygame.quit()

            if (lambda ev: event.type == ev)(pygame.MOUSEBUTTONDOWN):
                # If the user clicked on the input_box rect.
                if rect_ok.collidepoint(event.pos):
                    if inputs[0] and inputs[1] and inputs[2]:
                        return n, m, bombs
                if not inputs[0]:
                    if input_box_n.collidepoint(event.pos):
                        # Toggle the active variable.
                        text_n = ''
                        active_n = not active_n
                    else:
                        active_n = False
                        if text_n == '':
                            text_n = 'Podaj n'

                    if active_n:
                        color_n = color_active
                    else:
                        color_n = color_inactive
                        text_n = 'Podaj n'

                if not inputs[1]:
                    if input_box_m.collidepoint(event.pos):
                        # Toggle the active variable.
                        text_m = ''
                        active_m = not active_m
                    else:
                        active_m = False
                        if text_m == '':
                            text_m = 'Podaj m'
                    # Change the current color of the input box.
                    if active_m:
                        color_m = color_active
                    else:
                        color_m = color_inactive
                        text_m = 'Podaj m'

                if inputs[0] and inputs[1]:
                    if not inputs[2]:
                        if input_box_bombs.collidepoint(event.pos):
                            # Toggle the active variable.
                            text_bombs = ''
                            active_bombs = not active_bombs
                        else:
                            active_bombs = False
                            if text_bombs == '':
                                text_bombs = 'Bomby'
                        # Change the current color of the input box.
                        color_bombs = color_active if active_bombs else color_inactive

            if (lambda ev: event.type == ev)(pygame.KEYDOWN):
                if active_n:
                    if event.key == pygame.K_RETURN:
                        try:
                            # Blank input handling.
                            if not text_n:
                                raise NullInputException
                        except NullInputException as nie:
                            print(nie)
                            color_n = color_incorrect
                            active_n = False
                            text_n = 'Podaj liczbe!'
                            break
                        try:
                            # Non-digit input handling.
                            is_digit = True
                            for i in text_n:
                                if not i.isdigit():
                                    is_digit = False
                                    break
                            if not is_digit:
                                raise InvalidInputException(text_n)
                        except InvalidInputException as ve:
                            print(ve)
                            color_n = color_incorrect
                            active_n = False
                            text_n = 'Podaj liczbe!'
                            break
                        try:
                            if 2 <= int(text_n) <= 15:
                                # Accept and deactivate input.
                                color_n = color_correct
                                inputs[0] = True
                                print(text_n)
                                n = int(text_n)
                                active_n = not active_n
                                if not inputs[1]:
                                    active_n = False
                                    active_m = True
                                    text_m = ''
                                    color_m = color_active
                                    pygame.display.flip()
                                    break

                            else:
                                # Bad size handling.
                                raise ZleWymiaryException(text_n)

                            if inputs[0] and inputs[1]:
                                color_bombs = color_inactive
                        except ZleWymiaryException as e:
                            print(e)
                            color_n = color_incorrect
                            active_n = False
                            text_n = 'Zły wymiar! 1<n<16'
                            break
                    elif event.key == pygame.K_BACKSPACE:
                        text_n = text_n[:-1]
                    elif event.key == pygame.K_TAB:
                        # Switch between input boxes.
                        if not inputs[1]:
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
                        try:
                            # Blank input handling.
                            if text_m == "":
                                raise NullInputException
                        except NullInputException as nie:
                            print(nie)
                            color_m = color_incorrect
                            active_m = False
                            text_m = 'Podaj liczbe!'
                            break
                        try:
                            # Non-digit input handling.
                            is_digit = True
                            for i in text_m:
                                if not i.isdigit():
                                    is_digit = False
                                    break
                            if not is_digit:
                                raise InvalidInputException(text_m)
                        except InvalidInputException as ve:
                            print(ve)
                            color_m = color_incorrect
                            active_m = False
                            text_m = 'Podaj liczbe!'
                            break
                        try:
                            if 2 <= int(text_m) <= 15:
                                # Accept and deactivate input.
                                color_m = color_correct
                                inputs[1] = True
                                print(text_m)
                                m = int(text_m)
                                active_m = not active_m
                                if inputs[0]:
                                    active_m = False
                                    active_bombs = True
                                    text_bombs = ''
                                    color_bombs = color_active
                                    pygame.display.flip()
                                    break
                            else:
                                # Bad size handling.
                                raise ZleWymiaryException(text_m)
                            if inputs[0] and inputs[1]:
                                color_bombs = color_inactive
                        except ZleWymiaryException as e:
                            print(e)
                            color_m = color_incorrect
                            active_m = False
                            text_m = 'Zły wymiar! 1<m<16'
                    elif event.key == pygame.K_BACKSPACE:
                        text_m = text_m[:-1]
                    elif event.key == pygame.K_TAB:
                        # Switch between input boxes.
                        if not inputs[0]:
                            active_m = False
                            color_m = color_inactive
                            active_n = True
                            text_n = ''
                            text_m = 'Podaj m'
                            color_n = color_active
                            pygame.display.flip()
                    else:
                        text_m += event.unicode

                if active_bombs:
                    if inputs[0] and inputs[1]:
                        if event.key == pygame.K_RETURN:
                            try:
                                # Blank input handling.
                                if text_bombs == "":
                                    raise NullInputException
                            except NullInputException as nie:
                                print(nie)
                                color_bombs = color_incorrect
                                active_bombs = False
                                text_bombs = 'Podaj liczbe!'
                                break
                            try:
                                # Non-digit input handling.
                                is_digit = True
                                for i in text_bombs:
                                    if not i.isdigit():
                                        is_digit = False
                                        break
                                if not is_digit:
                                    raise InvalidInputException(text_bombs)
                            except InvalidInputException as ve:
                                print(ve)
                                color_bombs = color_incorrect
                                active_bombs = False
                                text_bombs = 'Podaj liczbe!'
                                break
                            try:
                                if 0 <= int(text_bombs) <= n * m:
                                    # Bad bomb input handling.
                                    color_bombs = color_correct
                                    inputs[2] = True
                                    print(text_bombs)
                                    bombs = int(text_bombs)
                                    # text_bombs = ''
                                    active_bombs = not active_bombs
                                else:
                                    raise BombsException(text_bombs)
                                if inputs[0] and inputs[1] and inputs[2]:
                                    ok = pygame.image.load("icons\\accept.png")
                            except BombsException as be:
                                print(be)
                                color_bombs = color_incorrect
                                active_bombs = False
                                text_bombs = '0<bombs<n*m!'
                                break
                            break
                        elif event.key == pygame.K_BACKSPACE:
                            text_bombs = text_bombs[:-1]
                        else:
                            text_bombs += event.unicode
                if event.key == pygame.K_RETURN:
                    if inputs[0] and inputs[1] and inputs[2]:
                        return n, m, bombs

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
            screen.blit(ok, rect_ok)
            # Blit the input_box rect.
            pygame.draw.rect(screen, color_n, input_box_n, 2)
            pygame.draw.rect(screen, color_m, input_box_m, 2)
            pygame.draw.rect(screen, color_bombs, input_box_bombs, 2)

            pygame.display.flip()
            clock.tick(30)
