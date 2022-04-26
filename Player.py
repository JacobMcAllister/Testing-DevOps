from pathlib import Path


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
                    self.name = data[0]
                    self.score = data[1]
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
        print("-----------------------\n  Player: " + self.name + "  Score: " + str(self.score) + "-----------------------\n" )



