import requests
import json


def get_info(url):
    return json.loads(requests.get(url).text)

if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/pokemon/charmander'
    print(get_info(url)['sprites']['other']['official-artwork']['front_default'])

    url = f'https://pokeapi.co/api/v2/pokemon-species/charmander'
    print(get_info(url)['flavor_text_entries'][0]['language']['name'])

    dic_flavor = get_info(url)['flavor_text_entries']


    lista_text_espanol = [elemento['flavor_text'] for elemento in get_info(url)['flavor_text_entries'] if elemento['language']['name'] == 'es']
    for i in lista_text_espanol:

        print(i)
        print('---------')
    
    print(len(lista_text_espanol))

    lista_set_text_espanol = set(lista_text_espanol)

    print(len(lista_set_text_espanol))