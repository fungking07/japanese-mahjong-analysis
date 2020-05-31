"""
Game class for holding mahjong game
"""

#from player import Player
import random

class Game:
    def __init__(self, dir_path):
        self.tiles = load_tiles(dir_path) # load all tiles from file for different mahjong
        self.num_tiles = len(self.tiles)
        self.hands = load_hands(dir_path) # load all hands from file for different mahjong
        self.players = []


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
            content[i] = {"hand":content[i][0], "pattern": content[i][1:]}

        return content


    def draw_tile(self):
        ind = random.randrange(0, len(self.tiles), 1)
        tile = self.tiles[ind]
        self.tiles.remove(tile)
        return tile


    def num_tiles(self):
        return self.num_tiles
