class land_card():
    def __init__(self, name, color_identity, land_type, flavor):
        self.name = name
        self.color_identity = color_identity
        self.mana_cost = 0
        self.land_type = land_type
        self.flavor = flavor
        self.tapped_status = 'untapped'


plains = land_card('Plains', '{W}', 'Basic Land', 'add one white mana to your manda pool')




class creature_card:
    def __init__(self, name, card_type, card_subtype, color_identity, flavor, mana_cost, counters=[], power=None, toughness=None, abilities=None):
        self.name = name
        self.card_type = card_type
        self.card_subtype = card_subtype
        self.color_identity = color_identity
        self.mana_cost = mana_cost
        self.power = power
        self.toughness = toughness
        self.abilities = []
        self.tapped_status = 'untapped'
    

