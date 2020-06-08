"""Głowny moduł programu"""
import pygame

import logic.fields as fd
import graphics.icons as ic
import graphics.icons_big as icB
import graphics.windows as wd
import graphics.squares as sq

pygame.init()

def print_array_state(array, n, m):
    """Print true or false if field is bomb in a matrix form."""
    for i in range(n):
        for j in range(m):
            print(array[i][j].is_bomb(), end=" ")
        print()


def print_mines_around(array, n, m):
    """Print mines around field in a matrix form."""
    for i in range(n):
        for j in range(m):
            print(array[i][j].get_mines_around(), end=" ")
        print()


def reset():
    """Reset game."""
    game_window.clear_window()
    game_window.reset_started()
    game_window.get_timer().update_time(0, game_window.get_screen())
    fd.Field.flagged_bomb_count = 0
    sq.Square.visible_count = 0
    sq.Square.flagged_count = 0
    minesweeper(n, m, bombs)


def minesweeper(n, m, bombs):
    """Creates game window and handle events."""
    fields = fd.get_matrix(n, m, bombs)
    game_window.reset_squares()
    squares = game_window.get_squares()

    timer = pygame.time.Clock()
    start_time = 0
    game_window.draw_scene()
    pygame.display.flip()
    run = True

    # Pomoc przy debugowaniu:
    print_array_state(fields, n, m)
    print_mines_around(fields, n, m)

    # Tablica do weryfikacji sekwencji xyzzy.
    xyzzy_sequence = [False, False, False, False, False]
    while run:
        for event in pygame.event.get():
            if (lambda ev: event.type == ev)(pygame.QUIT):
                run = False
                pygame.quit()
            elif (lambda ev: event.type == ev)(pygame.KEYDOWN):
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_r:
                    run = False
                    reset()

                # xyzzy event.
                elif keys[pygame.K_x]:
                    xyzzy_sequence[0] = True
                elif keys[pygame.K_y] and xyzzy_sequence[0]:
                    xyzzy_sequence[0] = False
                    xyzzy_sequence[1] = True
                elif keys[pygame.K_z] and xyzzy_sequence[1]:
                    xyzzy_sequence[1] = False
                    xyzzy_sequence[2] = True
                elif keys[pygame.K_z] and xyzzy_sequence[2]:
                    xyzzy_sequence[2] = False
                    xyzzy_sequence[3] = True
                elif keys[pygame.K_y] and xyzzy_sequence[3]:
                    xyzzy_sequence[3] = False
                    xyzzy_sequence[4] = True
                    game_window.xyzzy(fields)
                elif event.key != pygame.K_x or event.key != pygame.K_y or event.key != pygame.K_z:
                    print("inny przycisk klikniety")
                    for i in xyzzy_sequence:
                        i = False

            elif (lambda ev, evb: event.type == ev and event.button == evb)(pygame.MOUSEBUTTONDOWN, 1):

                if game_window.get_cat().get_cat().collidepoint(event.pos):
                    run = False
                    reset()
                for i in range(n):
                    for j in range(m):
                        if squares[i][j].get_rect().collidepoint(event.pos):
                            # Wystartowanie timera pod warunkiem ze zaczęto gre kliknięciem w jedno z pól.
                            if game_window.squares[0][0].visible_count == 0 and not game_window.get_started():
                                start_time = pygame.time.get_ticks()
                                click_time = pygame.time.get_ticks()
                                time = int(start_time - click_time)
                                game_window.get_timer().update_time(time, game_window.get_screen())
                                game_window.set_started()
                            game_window.reveal(fields, i, j, bombs)
                            break

            elif (lambda ev, evb: event.type == ev and event.button == evb)(pygame.MOUSEBUTTONDOWN, 3):

                for i in range(len(squares)):
                    for j in range(len(squares[i])):
                        if squares[i][j].get_rect().collidepoint(event.pos):
                            # Wystartowanie timera pod warunkiem ze zaczęto gre oflagowaniem jednego z pól.
                            if not game_window.get_started() and not game_window.squares[0][0].visible_count == n * m:
                                print("doszlo")
                                start_time = pygame.time.get_ticks()
                                click_time = pygame.time.get_ticks()
                                time = int(start_time - click_time)
                                game_window.get_timer().update_time(time, game_window.get_screen())
                                game_window.set_started()
                            # Dopóki gra jest wystartowana można klikać w przyciski.
                            if game_window.get_started():
                                if squares[i][j].get_clicked() == 0:
                                    fields[i][j].inc_bomb_flagged()
                                    if squares[i][j].get_size() > 60:
                                        squares[i][j].set_image(icB.flag)
                                    else:
                                        squares[i][j].set_image(ic.flag)
                                    squares[i][j].draw(screen)
                                    squares[i][j].set_clicked(2)
                                    game_window.check_if_win(fields, i, j, bombs)
                                    pygame.display.flip()

                                elif squares[i][j].get_clicked() == 2:
                                    fields[i][j].dec_bomb_flagged()
                                    if squares[i][j].get_size() > 60:
                                        squares[i][j].set_image(icB.qmark)
                                    else:
                                        squares[i][j].set_image(ic.qmark)
                                    squares[i][j].draw(screen)
                                    squares[i][j].set_clicked(3)
                                    pygame.display.flip()
                                elif squares[i][j].get_clicked() == 3:
                                    if squares[i][j].get_size() > 60:
                                        squares[i][j].set_image(icB.default)
                                    else:
                                        squares[i][j].set_image(ic.default)
                                    squares[i][j].draw(screen)
                                    squares[i][j].set_clicked(0)
                                    game_window.check_if_win(fields, i, j, bombs)
                                    pygame.display.update()
                                break
        screen.fill((255, 255, 255))
        game_window.draw_scene()

        # Aktualizacja timera pod warunkiem ze gra wystartowała i nie są ujawnione wszystkie pola.
        if game_window.get_started() and  game_window.squares[0][0].visible_count != n * m:
            click_time = pygame.time.get_ticks()
            time = int(click_time - start_time) // 1000
            game_window.get_timer().update_time(time, game_window.get_screen())
        timer.tick(60)


if __name__ == '__main__':
    # Wywołanie okna konfiguracji gry.
    n, m, bombs = wd.configuration()
    # Zdefiniowanie wysokosci top bara.
    TOP_BAR_HEIGHT = 75
    # Zainicjowanie obiektu okna gry i niezbędnych zmiennych.
    game_window = wd.GameWindow(n, m, TOP_BAR_HEIGHT)
    game_window.set_window()
    window = game_window.get_window()
    game_window.set_screen()
    screen = game_window.get_screen()
    pygame.display.set_caption("Saper")
    pygame.display.set_icon(ic.icon)
    SQUARE_HEIGHT = game_window.get_square_h()
    SQUARE_WIDTH = game_window.get_square_w()
    #Uruchomienie gry.
    minesweeper(n, m, bombs)
