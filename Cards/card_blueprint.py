import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Players import player_blueprint

class land_card():
    def __init__(self, name, color_identity, land_type, flavor):
        self.name = name
        self.card_type = 'land'
        self.color_identity = color_identity
        self.mana_cost = 0
        self.land_type = land_type
        self.flavor = flavor
        self.tapped_status = 'untapped'


plains = land_card('Plains', '{W}', 'Basic Land', 'add one white mana to your manda pool')




class creature_card:
    def __init__(self, name, card_type, card_subtype, color_identity, flavor, mana_cost, abilities = None, power=None, toughness=None):
        self.name = name
        self.card_type = card_type
        self.card_subtype = card_subtype
        self.color_identity = color_identity
        self.mana_cost = mana_cost
        self.power = power
        self.toughness = toughness
        self.abilities = abilities
        self.etb_trigger = []
        self.tapped_status = 'untapped'
    

leoes_da_savana = creature_card('Savannah Lions', 'creature', 'Cat', '{W}', '', ['{W}', '{W}', '{B}'], 1, 2, [])

def cast_card(player, card):

    mana_dork = card.mana_cost.copy()
    l = mana_dork
    if card.card_type == 'creature':
        for mana in range(len(card.mana_cost)):
            if card.mana_cost[mana] == '{W}':
                print (mana)
                if player.white_mana >= 1:
                    player.white_mana -= 1
                    mana_dork.remove('{W}')
                    print (l)
                    
                    
                    
                    print ("Creature casted")
                else:
                    print ("not enough White mana!!")


            if card.mana_cost[mana] == '{G}':
                print (mana)
                if player.green_mana >= 1:
                    player.green_mana -= 1
                    print ("Creature casted")
                else:
                    print ("not enough Green mana!!")


            if card.mana_cost[mana] == '{U}':
                print (mana)
                if player.blue_mana >= 1:
                    player.blue_mana -= 1
                    print ("Creature casted")
                else:
                    print ("not enough blue mana!!")


            if card.mana_cost[mana] == '{B}':
                print (mana)
                if player.white_mana >= 1:
                    player.white_mana -= 1
                    print ("Creature casted")
                else:
                    print ("not enough black mana!!")


            if card.mana_cost[mana] == '{R}':
                print (mana)
                if player.red_mana >= 1:
                    player.red_mana -= 1
                    print ("Creature casted")
                else:
                    print ("not enough Red mana!!")
            
    else:
        print ("land casted")



player_blueprint.gustavo.hand.append(leoes_da_savana)
print (player_blueprint.gustavo.generic_mana)
cast_card(player_blueprint.gustavo, leoes_da_savana)
print (player_blueprint.gustavo.generic_mana)