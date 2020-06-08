"""Module containing logic of the minesweeper."""
import random


class Field:
    """Represent single field logically."""
    flagged_bomb_count = 0

    def __init__(self, is_bomb, x, y, mines_around):
        self._is_bomb = is_bomb
        self._x = x
        self._y = y
        self._mines_around = mines_around

    def set_is_bomb(self):
        """Set field as a bomb."""
        self._is_bomb = True

    def inc_mines_around(self):
        """Set field as a bomb."""
        self._mines_around += 1

    def inc_bomb_flagged(self):
        """Increment Field.flagged_bomb_count."""
        if self._is_bomb:
            Field.flagged_bomb_count += 1

    def dec_bomb_flagged(self):
        """Decrement Field.flagged_bomb_count."""
        if self.is_bomb():
            Field.flagged_bomb_count -= 1

    def is_bomb(self):
        """Return True if field is a bomb."""
        return self._is_bomb

    def get_mines_around(self):
        """Return bombs around."""
        return self._mines_around


def get_matrix(n, m, bombs):
    """Return table of randomly generated bombs in matrix."""

    # Create n x m matrix of non-bomb fields.
    array = [[Field(False, i, j, 0) for j in range(m)] for i in range(n)]
    # Create array of every possible cord.
    possibilities = [[i, j] for j in range(m) for i in range(n)]

    for i in range(bombs):
        # For each bomb choose random cords from possibilities.
        chosen = random.choice(possibilities)
        # Remove this option from possibilities.
        possibilities.remove(chosen)
        # Set chosen field as a bomb.
        array[chosen[0]][chosen[1]].set_is_bomb()
        # Increment bomb counter of fields around the bomb.
        if (chosen[0] - 1) >= 0 and (chosen[1] - 1) >= 0 \
                and not array[chosen[0] - 1][chosen[1] - 1].is_bomb():
            array[chosen[0] - 1][chosen[1] - 1].inc_mines_around()

        if (chosen[1] - 1) >= 0 and not array[chosen[0]][chosen[1] - 1].is_bomb():
            array[chosen[0]][chosen[1] - 1].inc_mines_around()

        if chosen[0] + 1 < n and chosen[1] - 1 >= 0 \
                and not array[chosen[0] + 1][chosen[1] - 1].is_bomb():
            array[chosen[0] + 1][chosen[1] - 1].inc_mines_around()

        if chosen[0] - 1 >= 0 and not array[chosen[0] - 1][chosen[1]].is_bomb():
            array[chosen[0] - 1][chosen[1]].inc_mines_around()

        if chosen[0] + 1 < n and not array[chosen[0] + 1][chosen[1]].is_bomb():
            array[chosen[0] + 1][chosen[1]].inc_mines_around()

        if chosen[0] - 1 >= 0 and chosen[1] + 1 < m \
                and not array[chosen[0] - 1][chosen[1] + 1].is_bomb():
            array[chosen[0] - 1][chosen[1] + 1].inc_mines_around()

        if chosen[1] + 1 < m and not array[chosen[0]][chosen[1] + 1].is_bomb():
            array[chosen[0]][chosen[1] + 1].inc_mines_around()

        if chosen[0] + 1 < n and chosen[1] + 1 < m \
                and not array[chosen[0] + 1][chosen[1] + 1].is_bomb():
            array[chosen[0] + 1][chosen[1] + 1].inc_mines_around()

    return array
