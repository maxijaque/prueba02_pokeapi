from get_module import get_info


def get_base_pokemon(name):
      
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
    pokemon = get_info(url)
    if name == 'type-null':
        name = name_good('código-cero')
    else:
        name = name_good(pokemon['name'])
    id = pokemon['id']
    weight = pokemon['weight']
    list_stats = [pokemon['base_stat'] for pokemon in pokemon['stats']] 
    
    return name, id, weight, list_stats

def name_good(name):
    name = name.split('-')
    name = [item.capitalize() for item in name ]
    name = ' '.join(name)
    return name

def get_art_work(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
    art_work = get_info(url)['sprites']['other']['official-artwork']['front_default']

    return art_work

if __name__ == '__main__':
    print(get_info('https://pokeapi.co/api/v2/pokemon/25/').keys())
    print(get_info('https://pokeapi.co/api/v2/pokemon/25/')['forms'])
    print(get_base_pokemon(29)[0])
    print(get_art_work(25))
    print(name_good(get_base_pokemon(29)[0]))
    print(name_good('mew'))