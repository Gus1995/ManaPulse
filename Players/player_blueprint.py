
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class player():
    def __init__(self, name, life_point):
        self.name = name
        self.life_point = life_point
        self.battlefield = []
        self.deck = ['Land', 'Pássaros do Paraiso', 'Elfos de Llanowar', 'Raio']
        self.hand = []
        self.graveyard = []
        self.exile = []
        self.white_mana = 3
        self.blue_mana = 2
        self.black_mana = 1
        self.red_mana = 0
        self.green_mana = 0
        self.generic_mana = self.white_mana + self.blue_mana + self.black_mana + self.red_mana + self.green_mana
    

gustavo = player('Gustavo', 20)


