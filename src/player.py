"""
Player class as generic template
"""

class Player:
    def __init__(self, name, score, game, pos):
        self.game = game
        self.name = name
        self.tiles = []
        self.richi = [False,0]
        self.score = score
        self.dump = []
        self.str = [] # for tiles that put aside, dictionary with status and tiles
        self.menqian = True
        self.pos


    def set_richi(self):
        if self.menqian == True and self.game.num_tiles > 3:
            self.richi[0] = True
        return


    def get_history(self):
        game.sort_tiles(self.dump)
        return self.dump


    def score(self):
        return self.score


    def draw_tile(self):
        self.tiles.append(self.game.draw_tile())
        return


    def hand(self):
        return self.tiles


    def num_hands(self):
        return len(self.tiles)


    def sort_hand(self):
        self.tiles = self.game.sort_tiles(self.tiles)
        return


    def dump_tile(self, tile):
        if tile in self.tiles:
            #self.dump.append(tile)
            self.tiles.remove(tile)
            #self.dump = self.game.sort_tiles(self.dump)
            self.game.dump_tile(tile, self)
        else:
            print("Error: Invalid tile input")
        return


    def check(self):
        # check if winnable
        suits = self.game.detect_suits(self.tiles)

        # check for pattern
        return


    def ong(self, tile, pos):
        num = 0
        for h in self.tiles:
            if h == tile:
                num += 1

        if num == 3:
            return {"type":"gong", "tile":tile, "pos":pos}
        elif num == 2 and pos != self.pos:
            return {"type":"pong", "tile":tile, "pos":pos}
        else:
            return False


    def eat(self, tile):
        ls = []
        for i in self.tiles:
            if i[1] == tile[1] and i[0] != tile[0] and abs(int(i[0]) - int(tile[0])) <= 2:
                ls.append(i)

        flag = False
        newls = []

        if len(ls) < 2:
            return False
        else:
            nls = [ int(i[0]) for i in ls ]
            for i in range(len(nls)):
                diff = int(tile[0] - nls[i])
                if nls[i] + diff in nls:
                    flag = True
                    k = -1
                    ind = 0
                    while k < 0:
                        if nls[ind] == nls[i] + diff:
                            k = ind
                    newls.append([ls[i], ls[k])

        if len(newls) > 0:
            return newls
        else:
            return False
