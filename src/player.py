"""
Player class as generic template
"""

class Player:
    def __init__(self, name, score, game):
        self.game = game
        self.name = name
        self.tiles = []
        self.richi = False
        self.score = score
        self.dump = []
        self.str = [] # for tiles side put, dictionary with status and tiles


    def set_richi(self):
        self.richi = True
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
            self.dump.append(tile)
            self.tiles.remove(tile)
            self.dump = self.game.sort_tiles(self.dump)
        else:
            print("Error: Invalid tile input")
        return
