from get_module import get_info

def get_types_info(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
    pokemon = get_info(url)
    types = [ t['type']['name'] for t in pokemon['types']]

    return types
if __name__ == '__main__':
    print(get_types_info('charizard'))
