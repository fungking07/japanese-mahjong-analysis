"""
Game class for holding mahjong game
"""

from player import Player
from computer import Computer
from human import Human
import random

class Game:
    def __init__(self, dir_path):
        self.full_list = load_tiles(dir_path) # load all tiles from file for different mahjong
        self.tiles = self.full_list.copy()
        self.num_tiles = len(self.tiles)
        self.hands = load_hands(dir_path) # load all hands from file for different mahjong
        self.players = []
        self.suit = detect_suits(full_list)
        self.reserved = []


    def load_tiles(self, dir_path):
        # load tiles file
        path = dir_path + '/tiles.txt'
        with open(path, 'rt', encoding='utf8') as file:
            content = file.read()

        # split string to get all tiles
        content = content.split(' |,|\t|\n|;')
        return content


    def load_hands(self, dir_path):
        # load hands file
        path = dir_path + '/hands.txt'
        with open(path, 'rt', encoding='utf8') as file:
            content = file.readlines()

        # split to form list of hands
        for i in range(len(content)):
            content[i] = content[i].split(' |,|\t|;')
            content[i] = {"hand":content[i][0], "pattern": content[i][2:], "score":int(content[i][1])}

        return content


    def draw_tile(self):
        ind = random.randrange(0, len(self.tiles), 1)
        tile = self.tiles[ind]
        self.tiles.remove(tile)
        return tile


    def num_tiles(self):
        return self.num_tiles


    def add_player(self, player):
        if len(self.players) < 4 and isinstance(player, Player):
            self.players.append(player)
        else:
            print('player error')
        return


    def detect_suits(self, tile_list):
        # detect type of suits in the list of tiles
        suits = []
        for i in tile_list:
            if not i[-1] in suits:
                suits.append(i[-1])
        return suits


    def sort_tiles(self, tile_list):
        # follow orderings
        tile_list = tile_list.copy()
        tiles = [ [] for i in suit ]
        for i in range(len(suit)):
            for c in tile_list:
                if c[-1] == suit[i]
                tiles[i].append(c)
            for rmv in tiles[i]:
                tile_list.remove(rmv)


        def swap(a, b, list):
            tmp = list[a]
            list[a] = list[b]
            list[b] = tmp


        for ts in tiles:
            # iterative selection sort
            for i in range(len(ts)):
                tmp = ts[i]
                loc = i
                for j in range(i+1, len(ts)): # python range will not gen numbers if i+1 >= len(ts)
                    if ts[j] > tmp:
                        loc = j
                        tmp = ts[j]
                swap(i,j,ts)
        return


    def dump_tile(self, player, tile):
        #find player in pos
        ord = np.random.permutation(4)
        took = False
        for i in range(1, 4):
            loc = i + player.pos
            if loc >= 4:
                loc -= 4
            if took == False:
                took = self.players[loc].ong(tile, player.pos)

        took = self.players[player.pos - 1].eat(tile)

        if took == False:
            player.dump.append(tile)
        return


if __name__=='__main__':
    path = './'
    game = Game(path)
    game_mode = 'uninit'
    while not isnumeric(game_mode):
        game_mode = input("Enter number of players in 0-4: ")
    game_mode = int(game_mode)
    num_player = 0
    while num_player < game_mode:
        game.add_player(Human())
        num_player += 1
    while num_player < 4:
        game.add_player(Computer())
