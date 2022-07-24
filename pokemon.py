import requests


def get_names(dmg):
    return [x['name'] for x in dmg]


def get_dmg(type_from, type_to):
    r = requests.get(f'https://pokeapi.co/api/v2/type/{type_from}')

    result = r.json()
    damage = result['damage_relations']

    double_dmg = damage['double_damage_to']
    half_dmg = damage['half_damage_to']
    none_dmg = damage['no_damage_to']
    double_dmg = get_names(double_dmg)
    half_dmg = get_names(half_dmg)
    none_dmg = get_names(none_dmg)

    product = 1
    for p in type_to:
        if p in none_dmg:
            product = 0
            break
        elif p in double_dmg:
            product *= 2
        elif p in half_dmg:
            product /= 2
    return product

"""
type_from = 'fire'
type_to = ['grass']
print(get_dmg(type_from, type_to), end="x")
"""