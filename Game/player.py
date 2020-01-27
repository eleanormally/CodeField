class Player:
    x = 0
    y = 0
    colour = None
    health = 100

    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        if col == 'red':
            self.colour = [255, 43, 93]
        else:
            self.colour = [110, 136, 255]


    def activateAbil(dir):
        pass

    def passiveAbil():
        pass
