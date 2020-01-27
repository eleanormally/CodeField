class Heal:
    x = 0
    y = 0
    rad = 0
    healRate = 0
    runOut = False
    regen = False
    colour = [0,255,0]
    def __init__(self,x,y,rad=1,healRate=1,runOut=False,regen=False):
        self.x = x
        self.y = y
        self.rad = rad
        self.healRate = healRate
        self.runOut=runOut
        self.regen=regen
    def run(self):
        if runOut is not False:
            runout+=rege
    def heal(self,char):
        if self.runOut > 0 and char.distance(self.x,self.y) < self.rad:
            char.health+=self.healRate
            self.runOut-=self.healRate
