from get_module import get_info


def get_base_pokemon(name):
      
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
    pokemon = get_info(url)
    name = pokemon['name']
    id = pokemon['id']
    weight = pokemon['weight']
    hp = pokemon['stats'][0]['base_stat']
    attack = pokemon['stats'][1]['base_stat']
    defense = pokemon['stats'][2]['base_stat']
    special_attack = pokemon['stats'][3]['base_stat']
    special_defense = pokemon['stats'][4]['base_stat']
    speed = pokemon['stats'][5]['base_stat']
   
    return name, id, weight, hp, attack, defense, special_attack, special_defense, speed

if __name__ == '__main__':
    print(get_info('https://pokeapi.co/api/v2/pokemon/6/').keys())
    print(get_info('https://pokeapi.co/api/v2/pokemon/6/')['forms'])
    print(get_base_pokemon(6))