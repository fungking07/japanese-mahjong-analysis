from player import Player

class Human(Player):
    def __init__(self, name, score, game, pos):
        super().__init__(name, score, game, pos)


    def ong(self, tile, pos):
        pos = super().ong(tile, pos)
        if pos == False:
            return pos

        res = ""
        while len(res) <= 0:
            res = input("{} {} (y/n): ".format(pos['type'], tile))
            if res.casefold() == 'y':
                if pos['type'] == 'gong':
                    for i in range(3):
                        self.tiles.remove(tile)
                elif pos['type'] == 'pong':
                    for i in range(2):
                        self.tiles.remove(tile)

                self.str.append(pos)
                return True
            elif res.casefold() == 'n':
                return False
            else:
                print("Invalid input!!!")
                res = ""


    def eat(self, tile):
        pos = super().eat(tile)

        if pos == False:
            return False

        res = ""
        while len(res) <= 0:
            print("eat (Enter option number): ")
            for i in range(len(pos)):
                print("{}: {}".format(i+1, pos[i]))
            print("0: Not eat")
            res = input()
            try:
                res = int(res)
                if res == 0:
                    return False
                else:
                    res -= 1
                    self.str.append(pos[res])
                    return True
            except:
                res = ""
