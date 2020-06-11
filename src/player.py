'''
player class for mahjong game
Extend by human class, computer class, opponent class
'''
from game import Game

class Player:
    def __init__(self, dir_path):
        self.score = 20000
        self.hands = []
        self.melds = []
        self.river = [] # storing tile discarded
        self.num_hands = len(self.hands)+ len(self.melds)
        self.riichi_turn = 0 #立直, 0-> not riichi, for One-shot/ippatsu/一発 counting

    

    def display_hands(self):
        for i in self.hands:
            printf("%s ".format(i))
    
    def display_river(self):
        for i in self.river:
            printf("%s ".format(i))

    def sort_hands(self):
        # match pattern by init a big array?
        # eg a=[1,2,3,4] is assigned init
        # new input b = [3,3,1,4]
        # match b item corrsponeding to a and sort by array number of a
    
    def draw_hands(self):
        #this is use for drawing 13 tiles at turn 0 for each player
        count = 0
        for i in range(13):
            tile = Game.draw_tile()
            self.hands.append(tile)
        self.sort_hands()
    
    def draw_tile(self):
        tile = Game.draw_tile()
        #while tile in bouns:
        #   self.bouns.append(tile)
        #   tile = Game.draw_tile()
        self.hands.append(tile)

    def discard_hands(self):
        if not self.riichi_turn:
            d_tiles = input("Type the tile you want to discard:")
            while d_tiles not in range(self.hands):
                print("Wrong input. Please type a sequence number")
                d_tiles = input("Type the tiles you want to discard:")
            self.hands.remove(d_tiles)
        else:
            d_tiles = self.hands.pop()
            self.riichi_turn += 1
        self.river.append(d_tiles)

    
    def riichi(self):
        #check hand pattern if necessary
        self.discard_hands()

        self.score -= 1000
        self.riichi_turn = 1
        riichi_tile = self.river.pop()
        self.river.append("**"+riichi_tile+"**")


    def yaku(self, yaku_state):
        #this is related to pattern matching of yaku
        #yaku_state related to the yaku is in own turn or not


    def special_action(self, opponent):
        #Pongs Kongs Chows, related to melds


    def action(self):
        action = 'uninit'
        while not action.isdigit():
            action = input("Enter the action you want to do:")
        action = int(action)
        if action == 0:
            self.discard_hands()
        elif action == 1:
            self.riichi()
        elif action == 2:
            self.yaku(1)