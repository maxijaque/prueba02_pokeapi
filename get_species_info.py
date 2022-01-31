
from get_module import get_info
import random


def get_species(name):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{name}'
    dict_pok_spe = get_info(url)['flavor_text_entries']
    list_flavor_text = list(set([elemento['flavor_text'] for elemento in dict_pok_spe if elemento['language']['name'] == 'es']))
    flavor_text = random.choice(list_flavor_text)  
    a=  get_info(url)
    return flavor_text 

def get_special_ind(name):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{name}'
    
    is_mythical = get_info(url)['is_mythical']
    is_legendary = get_info(url)['is_legendary']
    is_baby = get_info(url)['is_baby']

    return is_mythical, is_legendary, is_baby

def get_evolves_previous(name):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{name}'
    evolves_from_species = get_info(url)['evolves_from_species']
    if evolves_from_species != None:
        evolves_from_species = evolves_from_species['name']

    return evolves_from_species


if __name__ == '__main__':
    print(get_info('https://pokeapi.co/api/v2/pokemon-species/4/').keys())
    print(get_species(4))

    print(get_special_ind(151))

    print(get_evolves_previous(7))
    

