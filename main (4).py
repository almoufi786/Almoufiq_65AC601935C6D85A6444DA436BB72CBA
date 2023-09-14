#define the base class player
class player:
    def play(self):
      print("The player is playing cricket.")

#Define The derived class Batsman
class Batsman(player):
    def play(self):
      print("The Batsman is batting.")

#Define The derived class Bowler
class Bowler(player):
    def play(self):
      print("The bowler is bowling.")

#create object of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()
#call The play() method for each object
batsman.play()
bowler.play()