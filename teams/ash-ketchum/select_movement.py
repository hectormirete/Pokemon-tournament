from typing import List
from models.movement import Movement
from models.pokemon import Pokemon
from pokedex import Pokedex


def select_move(attacker_moves: List[Movement], attacker: Pokemon, defender: Pokemon):
    pd = Pokedex()

    def str_to_float(x: str):
        try:
            return float(x.replace("%", ""))
        except:
            return 1.0
    
    for move in attacker_moves:
        print(move.type, defender.type1, pd.get_multiplier(move.type, defender.type1))
        print(move.type, defender.type2, pd.get_multiplier(move.type, defender.type2))
        print(max(pd.get_multiplier(move.type, defender.type1), pd.get_multiplier(move.type, defender.type2)))
    
    move = max(
        attacker_moves,
        key=lambda x: float(x.power) * str_to_float(x.accuracy) * float(max(pd.get_multiplier(x.type, defender.type1), pd.get_multiplier(x.type, defender.type2)))
    )
    return move