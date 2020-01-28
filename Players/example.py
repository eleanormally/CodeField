###this is an example on how to set up a player
import sys
sys.path.append('../Game')
from player import Player


###IMPORTANT: USE CLASS NAME CustomPlayer. It will not import with a different name
class CustomPlayer(Player):
    def think(limitedGameBoard,comms,limitedOtherTeam,team):
        pass
