
from get_module import get_info
import random
from get_base_info import name_good

def get_species(name):
    url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{name}'
    url_species = get_info(url_pokemon)['species']['url'] 
    dict_pok_spe = get_info(url_species)['flavor_text_entries']
    list_flavor_text = [elemento['flavor_text'].replace('\n', ' ') for elemento in dict_pok_spe if elemento['language']['name'] == 'es']
    flavor_text = random.choice(list_flavor_text)  
    return flavor_text 

def get_special_ind(name):
    url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{name}'
    url_species = get_info(url_pokemon)['species']['url'] 
    
    list_special = []
    is_mythical = get_info(url_species)['is_mythical']
    if is_mythical == True:
        is_mythical = 'mythical'
        list_special.append(is_mythical)
    
    is_legendary = get_info(url_species)['is_legendary']
    if is_legendary == True:
        is_legendary = 'legendary'
        list_special.append(is_legendary)

    is_baby = get_info(url_species)['is_baby']
    if is_baby == True:
        is_baby = 'baby'
        list_special.append(is_baby)

    return list_special

def get_evolves_previous(name):
    url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{name}'
    url_species = get_info(url_pokemon)['species']['url']  
    evolves_from_species = get_info(url_species)['evolves_from_species']
    if evolves_from_species != None:
        evolves_from_species = evolves_from_species['name']
    else:
        evolves_from_species = ''
    evolves_from_species = name_good(evolves_from_species)
    return evolves_from_species


if __name__ == '__main__':
    print(get_info('https://pokeapi.co/api/v2/pokemon-species/4/').keys())
    print(get_species(122))

    print(get_special_ind(122))

    print(get_evolves_previous('deoxys-normal'))
    

