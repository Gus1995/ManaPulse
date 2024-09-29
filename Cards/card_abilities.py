import card_blueprint
import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Players import player_blueprint






def draw_card(target, number_cards):
    
    for i in range(number_cards):
        card = target.deck[int(len(player_blueprint.gustavo.deck))-1]
        target.deck.pop()
        target.hand.append(card)
        i += 1

def mill_card(target, number_cards):
    
    for i in range(number_cards):
        card = target.deck[int(len(player_blueprint.gustavo.deck))-1]
        target.deck.pop()
        target.graveyard.append(card)
        i += 1

def add_mana(target, mana):
    
    matches = re.findall(r'(\{R\}|\{G\}|\{W\}|\{U\}|\{B\}|\{1\}|\{2\}|\{3\}|\{4\}|\{5\}|\{6\}|})', mana)
    for i in range(len(matches)):
        symbol = matches[i]
        print (symbol)
        if symbol == '{W}':         
            target.white_mana += 1   
        elif symbol == '{U}':
            target.blue_mana += 1
        elif symbol == '{B}':
            target.black_mana += 1
        elif symbol == '{R}':
            target.red_mana += 1
        elif symbol == '{G}':
            target.green_mana += 1
        elif symbol == '{1}':
            target.generic_mana += 1
        elif symbol == '{2}':
            target.generic_mana += 2
        i += 1

def tap_land(target_player, land):

    color = land.color_identity
    add_mana(target_player, color)

def empty_mana_pool(target):
    target.white_mana = 0   
    target.blue_mana = 0
    target.black_mana = 0
    target.red_mana = 0
    target.green_mana = 0
    target.generic_mana = 0
    target.generic_mana = 0




def target_gains_power_toughness(target, power, toughness):
    target.power += power
    target.toughness += toughness

def target_gains_power_abbility(target, ability, until_endof):
    target.abilities.append(ability)
    


print(player_blueprint.gustavo.white_mana)
print(player_blueprint.gustavo.blue_mana)
print(player_blueprint.gustavo.red_mana)
print(player_blueprint.gustavo.green_mana)
print(player_blueprint.gustavo.black_mana)
print(player_blueprint.gustavo.generic_mana)