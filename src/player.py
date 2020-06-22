"""
Player class as generic template
"""

class Player:
    def __init__(self, name, score, game):
        self.game = game
        self.name = name
        self.tiles = []
        self.richi = [False,0]
        self.score = score
        self.dump = []
        self.str = [] # for tiles that put aside, dictionary with status and tiles
        self.menqian = True


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
            #self.tiles.remove(tile)
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
