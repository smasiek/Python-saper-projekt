"""Module implementing single square graphical representation"""
import pygame

class Square:
    """Represent single field in GUI"""
    visible_count = 0
    flagged_count = 0

    def __init__(self, y, x, height, width, clicked, image):
        """
        x,y - koordynaty pola
        height,width - wymiary pola
        clicked - 0-nie,1-LPM,2-PPMx1,3-PPMx2
        """
        self._rect = pygame.rect.Rect(x, y + 75, height, width)
        self._x = x
        self._y = y + 75
        self._height = height
        self._width = width
        self._clicked = clicked
        self._image = image

    def get_px_x(self):
        """Return coord x of square."""
        return int(self._x)

    def get_px_y(self):
        """Return coord y of square."""
        return int(self._y)

    def get_size(self):
        """Return lenght of side of square."""
        return self._height

    def draw(self, screen):
        """Blits actual image of square."""
        screen.blit(self._image, (self.get_px_x(), self.get_px_y()))

    def set_image(self, image):
        """Update image of square."""
        self._image = image

    def set_clicked(self, click):
        """Handle square clicks."""
        # Protect from being clickable after being clicked.
        if self._clicked != 1:
            if click == 1:
                self._clicked = click
                Square.visible_count += 1
            elif click == 2:
                self._clicked = click
                Square.flagged_count += 1
            elif click == 3:
                self._clicked = click
                Square.flagged_count -= 1
            elif click == 0:
                self._clicked = click

    def get_clicked(self):
        """Return state of square"""
        return self._clicked

    def get_rect(self):
        """Return rect object of square"""
        return self._rect

    @staticmethod
    def reset_flagged_count():
        """Reset flagged squares counter, used in game reset."""
        Square.flagged_count = 0
