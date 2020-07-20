"""
Game class for holding mahjong game
"""

from player import Player
from computer import Computer
from human import Human
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


    def add_player(self, player):
        if len(self.players) < 4 and isinstance(player, Player):
            self.players.append(player)
        else:
            print('player error')
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
