from string import Template
import sys
import json
import requests
from poke_validation import validate
from get_module import get_info
import random
from get_base_info import get_base_pokemon, get_art_work
from get_species_info import get_evolves_previous, get_species
from get_types import get_types_info
from get_damage_relations import get_damage_relations, genera_span
from show import show_pics

name = input('Introduzca el nombre del Pokémon a procesar: ')
name = validate(name)

pok_name, pok_id, pok_weight, list_stats = get_base_pokemon(name)
pok_hp, pok_at, pok_de, pok_ate, pok_dee, pok_ve = list_stats
pok_img = get_art_work(name)

pok_stage_previous = get_evolves_previous(name)
if pok_stage_previous != '':
    pok_stage_previous = f'Etapa Previa: {pok_stage_previous}'
pok_flavor_text =get_species(name)
list_type = get_types_info(name)
span_type = genera_span(list_type)
list_damage_relations = get_damage_relations(name)
double_damage_to, double_damage_from, half_damage_from, half_damage_to, no_damage_from, no_damage_to = list_damage_relations
span_double_damage_to = genera_span(double_damage_to)
span_double_damage_from = genera_span(double_damage_from)
span_half_damage_to = genera_span(half_damage_to)
span_half_damage_from = genera_span(half_damage_from)
span_no_damage_from = genera_span(no_damage_from)
span_no_damage_to = genera_span(no_damage_to)

with open('base.html', 'r', encoding='utf-8') as infile:
    entrada = infile.read()

document_template =Template(entrada)

document_template_nuevo = document_template.safe_substitute(
    pok_id = pok_id,
    pok_name = pok_name,
    pok_img = pok_img,
    pok_stage_previous = pok_stage_previous,
    pok_hp = pok_hp,
    pok_at = pok_at,
    pok_de = pok_de,
    pok_ate = pok_ate,
    pok_dee = pok_dee,
    pok_ve = pok_ve,
    span_type = span_type,
    pok_flavor_text = pok_flavor_text,
    span_double_damage_to = span_double_damage_to, 
    span_double_damage_from = span_double_damage_from,
    span_half_damage_to = span_half_damage_to,
    span_half_damage_from = span_half_damage_from,
    span_no_damage_from = span_no_damage_from,
    span_no_damage_to = span_no_damage_to
)

with open('salida.html', 'w', encoding='utf-8') as outfile:
    outfile.write(document_template_nuevo)


show_pics(document_template_nuevo, 'output')
