from get_module import get_info
from get_types import get_types_info


def get_for_for(lista, damage_relations):
    damage_relation = list(set([i['name'] for elemento in lista for i in get_info(elemento)['damage_relations'][damage_relations]]))
    return damage_relation


def get_damage_relations(name):
    list_types = get_types_info(name)
    url = 'https://pokeapi.co/api/v2/type/'
    resultados = get_info(url)['results']
    listas_url = [elementos['url'] for elementos in resultados if elementos['name'] in list_types]
    double_damage_to =  get_for_for(listas_url, 'double_damage_to')
    double_damage_from = get_for_for(listas_url, 'double_damage_from')
    half_damage_from = get_for_for(listas_url,'half_damage_from')
    half_damage_to =  get_for_for(listas_url,'half_damage_to')
    no_damage_from = get_for_for(listas_url,'no_damage_from')
    no_damage_to = get_for_for(listas_url,'no_damage_to')

    return double_damage_to, double_damage_from, half_damage_to, half_damage_from, no_damage_from, no_damage_to

if __name__ == '__main__':
    print(get_damage_relations(6))