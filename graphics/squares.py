import pygame



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

    def getSize(self):
        return self._height

    def draw(self,screen):
        screen.blit(self._image, (self.getPxX(),self.getPxY()))

    #def incVisibleCount(self):
    #    self.visibleCount+=1

    def setImage(self,image):
        self._image=image

    def setClicked(self,click):

        if click==1:

            self._clicked = click
            Square.visibleCount += 1
        if click==2:
            self._clicked = click
            Square.flaggedCount += 1
            #Square.visibleCount += 1 #test do usuniecia

        if click==3:
            self._clicked = click
            Square.flaggedCount -= 1
        if click==0:
            self._clicked = click

            #Square.visibleCount -= 1 #test do timera do usuniecia jesl nie dziala
        print("Flagged count:" ,Square.flaggedCount)
        print(Square.visibleCount)

    def getClicked(self):
        return self._clicked

    def getRect(self):
        return self._rect

    def getVisibleCount(self):
        return self.visibleCount

    def resetFlaggedCount(self):
        Square.flaggedCount=0

