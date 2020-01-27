import pyglet
from boardLoader import Board
import cRender


boardName = 'testBoard'
if type(boardName) is not str:
    print('input board name')
    boardName = input()
mainBoard = Board(boardName)

xsize = 1920
ysize = 1080

xc = len(mainBoard.gameBoard[0])
yc = len(mainBoard.gameBoard)

if(xsize/xc<(ysize-50)/yc):
    tileSize = int(xsize/xc)
else:
    tileSize = int((ysize-50)/yc)

game_window = pyglet.window.Window(xsize,ysize)

rScore = pyglet.text.Label(text='0',x=xsize/2+100,y=ysize-25,anchor_x='center')
bScore = pyglet.text.Label(text='0',x=xsize/2-100,y=ysize-25,anchor_x='center')


def update(self):
    game_window.clear()
    rScore.draw()
    bScore.draw()
    #display board
    tx = 0
    ty = 0

    for r in mainBoard.gameBoard:
        tx = (xsize-tileSize*xc)/2
        for c in r:
            cRender.draw_rect(tx,ty,tileSize,tileSize,c.colour)
            tx+=tileSize
        ty+=tileSize




if __name__ == '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()
else:
    print('error: not running as main')
