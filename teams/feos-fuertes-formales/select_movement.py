from shutil import move
from models.pokemon import Pokemon
from models.movement import Movement
from typing import List
from pokedex import Pokedex

def select_move(attacker_moves: List[Movement], attacker:Pokemon, defender: Pokemon):
    # Load pokedex to be able to compute damage type multipliers
    pokedex = Pokedex()

    # Get the damage type multipliers by move
    multiplied_attack_power = [
        pokedex.get_multiplier(move.type, defender.type1) *
            pokedex.get_multiplier(move.type, defender.type2)
        for move in attacker_moves
    ]

    # Find the most damaging move
    maximum_multiplied_attack_power = max(multiplied_attack_power)
    best_move = multiplied_attack_power.index(maximum_multiplied_attack_power)
    
    # Destroy your enemies
    return attacker_moves[best_move]