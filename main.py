import random

import pygame, sys

pygame.init()

class Main:
    def __init__(self):
        self.xMatPos = 0
        self.yMatPos = 0
        self.mat = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        self.turn = random.randint(1, 2)
        self.shapeColor = (25, 121, 169)

    def drawElements(self):
        pygame.draw.line(screen, (31, 41, 54), (495, 110), (495, 710), 10)
        pygame.draw.line(screen, (31, 41, 54), (695, 110), (695, 710), 10)
        pygame.draw.line(screen, (31, 41, 54), (300, 305), (897, 305), 10)
        pygame.draw.line(screen, (31, 41, 54), (300, 505), (897, 505), 10)

        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                if(self.mat[i][j]==1):
                    self.shapeColor = (25, 121, 169)
                    self.drawCross(320 + (200*j), 130 + (200*i))
                elif(self.mat[i][j]==2):
                    self.shapeColor = (204, 0, 0)
                    self.drawCircle(398 + (200*j), 208 + (200*i))

        self.gameFont = pygame.font.Font("ARCADECLASSIC.ttf", 100)
        self.scoreText = "Tic Tac Toe"
        self.scoreSurf = self.gameFont.render(self.scoreText, True, (0, 0, 0))
        self.scoreRect = self.scoreSurf.get_rect(center = (600, 50))
        screen.blit(self.scoreSurf, self.scoreRect)

    def updateMatrix(self, x, y, z):
        self.mat[x][y] = z

    def getValue(self, x, y):
        return self.mat[x][y]

    def drawCross(self, x, y):
        pygame.draw.line(screen, self.shapeColor, (x, y), (x + 150, y + 150), 10)
        pygame.draw.line(screen, self.shapeColor, (x+150, y), (x, y+150), 10)

    def drawCircle(self, x, y):
        pygame.draw.circle(screen, self.shapeColor, (x, y), 75, 5)

    def setTurn(self, x):
        self.turn = x

    def gameOver(self):

        if(self.mat[0][0] == self.mat[0][1] and self.mat[0][1] == self.mat[0][2] and self.mat[0][0] != 0):
            return True
        if(self.mat[1][0] == self.mat[1][1] and self.mat[1][1] == self.mat[1][2] and self.mat[1][0] != 0):
            return True
        if(self.mat[2][0] == self.mat[2][1] and self.mat[2][1] == self.mat[2][2] and self.mat[2][0] != 0):
            return True

        if(self.mat[0][0] == self.mat[1][0] and self.mat[1][0] == self.mat[2][0] and self.mat[0][0] != 0):
            return True
        if(self.mat[0][1] == self.mat[1][1] and self.mat[1][1] == self.mat[2][1] and self.mat[0][1] != 0):
            return True
        if(self.mat[0][2] == self.mat[1][2] and self.mat[1][2] == self.mat[2][2] and self.mat[0][2] != 0):
            return True

        if(self.mat[0][0] == self.mat[1][1] and self.mat[1][1] == self.mat[2][2] and self.mat[0][0] != 0):
            return True
        if(self.mat[0][2] == self.mat[1][1] and self.mat[1][1] == self.mat[2][0] and self.mat[0][2] != 0):
            return True


        
        return False

    def checkButtons(self, mousePos):

        xGrid = 0
        yGrid = 0

        if mousePos[0] > 300 and mousePos[0] < 900 and mousePos[1] >110 and mousePos[1] < 710:
            if mousePos[0] > 300 and mousePos[0] < 500:
                yGrid = 0
            elif mousePos[0] > 500 and mousePos[0] < 700:
                yGrid = 1
            elif mousePos[0] > 700 and mousePos[0] < 900:
                yGrid = 2


            if mousePos[1] > 110 and mousePos[1] < 310:
                xGrid = 0
            elif mousePos[1] > 310 and mousePos[1] < 510:
                xGrid = 1
            elif mousePos[1] > 510 and mousePos[1] < 710:
                xGrid = 2

            if(self.mat[xGrid][yGrid]==0):
                self.mat[xGrid][yGrid] = self.turn
                return True

        return False


screen = pygame.display.set_mode((1200, 760))
clock = pygame.time.Clock()

xPos = 300
yPos = 110

gameScreenBord = pygame.Surface((610, 610))
gameScreenBord.fill((167, 206, 209))
gameScreen = pygame.Surface((600, 600))
gameScreen.fill((38, 52, 69))

updateScreen = pygame.USEREVENT

main = Main()
#pygame.time.set_timer(updateScreen, 10)
endText = ""

def printEnd(endText):
    endFont = pygame.font.Font("ARCADECLASSIC.ttf", 20)
    endText = " ' " + endText + " ' " + " Has Won The Game"
    endSurf = endFont.render(endText, True, (240, 244, 255))
    endRect = endSurf.get_rect(center=(1050, 700))
    screen.blit(endSurf, endRect)

while True:
    for event in pygame.event.get():
        pygame.time.set_timer(updateScreen, 60)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if(not main.gameOver()):
            if(event.type == pygame.MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                changeTurn = main.checkButtons(pos)
                if(changeTurn):
                    if main.turn == 1:
                        main.turn = 2
                    elif main.turn == 2:
                        main.turn = 1
        else:
            if main.turn == 1:
                endText = "O"
            else:
                endText = "X"



    screen.fill((38, 52, 69))

    screen.blit(gameScreenBord, (xPos-5, yPos-5))
    screen.blit(gameScreen, (xPos, yPos))
    main.drawElements()

    if main.gameOver():
        printEnd(endText)

    pygame.display.update()

    clock.tick(60)
