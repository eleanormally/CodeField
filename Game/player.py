from wall import Wall
class Player:
    x = 0
    y = 0
    colour = None
    health = 100
    damage = 15

    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        if col == 'red':
            self.colour = [255, 43, 93]
        else:
            self.colour = [110, 136, 255]

    #this is the function that is called every frame so that the
    #player can make decisions and act upon them.
    #you are given a list of communications in the team, which are lists of max length 3 and from range 0 to 255
    #you are also given a limited game board, which acts as what the player can see, shielding things in fog of war
    #this is the function you will edit
    def think(self,limitedGameBoard,comms,limitedOtherTeam,team):
        pass

    def activateAbil(dir):
        pass
    def passiveAbil():
        pass

    def attack(enemy):
        enemy.health-=damage


    def moveUp(self,limitedGameBoard,limitedOtherTeam,team):
        if self.y == len(limitedGameBoard)-1:
            return
        for p in team:
            if p.x == self.x and p.y == self.y+1:
                return
        for p in limitedOtherTeam:
            if p.x == self.x and p.y == self.y+1:
                attack(p)
                return
        if isinstance(limitedGameBoard[self.y+1][self.x],Wall):
            return
        self.y+=1


    def moveDown(self,limitedGameBoard,limitedOtherTeam,team):
        if self.y == 0:
            return
        for p in team:
            if p.x == self.x and p.y == self.y-1:
                return
        for p in limitedOtherTeam:
            if p.x == self.x and p.y == self.y-1:
                attack(p)
                return
        if isinstance(limitedGameBoard[self.y-1][self.x],Wall):
            return
        self.y-=1


    def moveLeft(self,limitedGameBoard,limitedOtherTeam,team):
        if self.x == 0:
            return
        for p in team:
            if p.x == self.x-1 and p.y == self.y:
                return
        for p in limitedOtherTeam:
            if p.x == self.x-1 and p.y == self.y:
                attack(p)
                return
        if isinstance(limitedGameBoard[self.y][self.x-1],Wall):
            return
        self.x-=1


    def moveRight(self,limitedGameBoard,limitedOtherTeam,team):
        if self.x == len(limitedGameBoard[0])-1:
            return
        for p in team:
            if p.x == self.x+1 and p.y == self.y:
                return
        for p in limitedOtherTeam:
            if p.x == self.x+1 and p.y == self.y:
                attack(p)
                return
        if isinstance(limitedGameBoard[self.y][self.x+1],Wall):
            return
        self.x+=1
