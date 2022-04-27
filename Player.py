from pathlib import Path
import os

class Player(object):
    def __init__(self, name = ""):
        if not name == "":
            self.fle = Path("." + "/" + "players" + "/" + name + ".txt")
            self.fle.touch(exist_ok=True)
            with open(self.fle, "r+") as f:
                data = f.readlines()

                if not data:
                    #  Insert code to find player
                    self.name = name
                    f.writelines(name+"\n")
                    self.score = 0
                    f.writelines("0\n")
                else:
                    self.name = data[0].removesuffix('\n')                  
                    self.score = int(data[1])
        else:
            self.name = "Player"
            self.score = 0

    def updateScore(self):
        self.score = int(self.score) + 1
        with open(self.fle, "r+") as f:
            data = f.readlines()
            data[1] = str(self.score)
            f.seek(0,0)
            f.writelines(data)

    def displayPlayer(self):
        print("-----------------------------------------\n    Player: " + self.name + "\n    Score: " + str(self.score) + "\n-----------------------------------------\n" )

    def listPlayers():
        players = [f for f in os.listdir(Path("." + "/" + "players" + "/")) if os.path.isfile(os.path.join(Path("." + "/" + "players" + "/"), f))]

        print("C U R R E N T  P L A Y E R S\n-----------------------------------------")
        for p in players:
            print("   " + p.removesuffix(".txt"))
        print("-----------------------------------------\n")