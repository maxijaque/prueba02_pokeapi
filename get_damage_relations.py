from get_module import get_info
from get_types import get_types_info
import data as d

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
    half_damage_to = get_for_for(listas_url,'half_damage_to')
    half_damage_from =  get_for_for(listas_url,'half_damage_from')
    no_damage_from = get_for_for(listas_url,'no_damage_from')
    no_damage_to = get_for_for(listas_url,'no_damage_to')

    return double_damage_to, double_damage_from, half_damage_to, half_damage_from, no_damage_from, no_damage_to

def genera_span(lista):
    d.diccionario_es
    span_str = ''
    for item in lista:
        item_es = (d.diccionario_es.get(item)).capitalize()

        span_str = span_str + f'<span class="label {item}">{item_es}</span>\n'

    return span_str

if __name__ == '__main__':
    print(get_damage_relations(6))
    print(genera_span(get_damage_relations(6)[0]))

    