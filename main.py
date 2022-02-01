# Se importan las librerias se utilizaran.
from string import Template
from poke_validation import validate
from get_module import get_info
from get_base_info import get_base_pokemon, get_art_work
from get_species_info import get_evolves_previous, get_species
from get_types import get_types_info
from get_damage_relations import get_damage_relations, genera_span
from show import show_pics

# Se solicita al usuario que ingrese un nombre valido de un pokémon.
name = input('Introduzca el nombre del Pokémon a procesar: ')
name = validate(name)

# Se obtiene siguiente informacion del pokémon: nombre, id, peso, y una lista de estadisticas.
pok_name, pok_id, pok_weight, list_stats = get_base_pokemon(name)

# Se desenrolla la lista de estadisticas: hp, ataque, defensa, ataque especial, defensa especial y velocidad.
pok_hp, pok_at, pok_de, pok_ate, pok_dee, pok_ve = list_stats

# Se obtiene el url de artwork front default del pokemon ingresado.
pok_img = get_art_work(name)

# Se obtiene el pokémon previo si esque existe. Luego se crea un string para introducirlo en el html de ser verdadero.
pok_stage_previous = get_evolves_previous(name)
if pok_stage_previous != '':
    pok_stage_previous = f'Etapa Previa: {pok_stage_previous}'

# Se obtiene el mensaje de forma aleatoria con la función get_species del modulo  creado get_species_info
pok_flavor_text =get_species(name)

# Se obtiene la lista de tipos, incluido si son legendarios, míticos y/o bebé
list_type = get_types_info(name)

# Se genera el span de las diferentes lista de tipo
span_type = genera_span(list_type)
list_damage_relations = get_damage_relations(name)
double_damage_to, double_damage_from, half_damage_from, half_damage_to, no_damage_from, no_damage_to = list_damage_relations
span_double_damage_to = genera_span(double_damage_to)
span_double_damage_from = genera_span(double_damage_from)
span_half_damage_to = genera_span(half_damage_to)
span_half_damage_from = genera_span(half_damage_from)
span_no_damage_from = genera_span(no_damage_from)
span_no_damage_to = genera_span(no_damage_to)

# Se la plantilla html donde ira toda la información recopilada
with open('base.html', 'r', encoding='utf-8') as infile:
    entrada = infile.read()

# Se transforma en un Template
document_template =Template(entrada)

# Se sustituye los elementos $elementos
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

## Se crea un archivo html permanente
# with open('salida.html', 'w', encoding='utf-8') as outfile:
#     outfile.write(document_template_nuevo)

# Se crea una archivo temporal html el cual se abre en el navegador y es eliminado
show_pics(document_template_nuevo, 'output')
