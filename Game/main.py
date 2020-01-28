import pyglet
from boardLoader import Board
import cRender
import time

boardName = 'testBoard'
playerName = 'example'
if type(boardName) is not str:
    print('input board name')
    boardName = input()

if type(playerName) is not str:
    print('input player name')
    playerName = input()

mainBoard = Board(boardName,playerName)

xsize = 1700
ysize = 800

xc = len(mainBoard.gameBoard[0])
yc = len(mainBoard.gameBoard)

if(xsize/xc<(ysize-50)/yc):
    tileSize = int(xsize/xc)
else:
    tileSize = int((ysize-50)/yc)

game_window = pyglet.window.Window(xsize,ysize)

rScore = pyglet.text.Label(text='0',x=xsize/2+100,y=ysize-25,anchor_x='center')
bScore = pyglet.text.Label(text='0',x=xsize/2-100,y=ysize-25,anchor_x='center')

sPoint = (xsize-tileSize*xc)/2
pStartX = sPoint+tileSize/3

def update(self):
    game_window.clear()
    rScore.draw()
    bScore.draw()
    #display board
    ty = 0

    for r in mainBoard.gameBoard:
        tx = sPoint
        for c in r:
            cRender.draw_rect(tx,ty,tileSize,tileSize,c.colour)
            tx+=tileSize
        ty+=tileSize

    #grid marker display
    lineWidth=tileSize/20
    ty = tileSize-lineWidth/2
    for i in range(len(mainBoard.gameBoard)-1):
        cRender.draw_rect(sPoint,ty,xsize-sPoint*2,lineWidth,[150,150,150])
        ty+=tileSize
    tx = sPoint+tileSize-lineWidth/2
    for i in range(len(mainBoard.gameBoard[0])-1):
        cRender.draw_rect(tx,0,lineWidth,tileSize*yc,[150,150,150])
        tx+=tileSize


    #player display
    for p in mainBoard.playerList:
        cRender.draw_rect(pStartX+p.x*tileSize,tileSize/3+p.y*tileSize,tileSize/3,tileSize/3,p.colour)
        p.moveUp(mainBoard.gameBoard,[],mainBoard.playerList)

    time.sleep(0.3)




if __name__ == '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()
else:
    print('error: not running as main')
