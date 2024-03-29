from functions import functions
import re
import sys
from itertools import combinations
from typing import List


def data_processing():
    tab = functions.clear_input("input.txt", " ")
    return {tab[i][0]: {'speed': int(tab[i][3]), 'duration': int(tab[i][6]), 'resting_time': int(tab[i][-2]), 'time_to_go' : 1} for i in range(len(tab))}


def ex14():
    reindeers = data_processing()
    distances = {key: 0 for key in reindeers.keys()}
    points = {key: 0 for key in reindeers.keys()}

    for clock in range(1, 2504):
        for renne in reindeers.keys():
            if reindeers[renne]['time_to_go'] + reindeers[renne]['duration'] > clock >= reindeers[renne]['time_to_go']:
                distances[renne] += reindeers[renne]['speed']
            elif clock == reindeers[renne]['time_to_go'] + reindeers[renne]['duration']:
                reindeers[renne]['time_to_go'] += reindeers[renne]['resting_time'] + reindeers[renne]['duration']

        for renne in reindeers.keys():
            if distances[renne] == max(distances.values()):
                points[renne] += 1
    return max(distances.values()), max(points.values())


def ex15():
    tab = functions.clear_input("input.txt", ":")
    ingredients = {tab[i][0]: [int(x[-2:]) for x in tab[i][1].split(',')] for i in range(len(tab))}
    print(ingredients)
    t = [[3, 0, 0, -3, 2], [-3, 3, 0, 0, 9], [-1, 0, 4, 0, 1], [0, 0, -2, 2, 8]]
    max_score = 0
    for i in range(0, 100):
        for j in range(0, 100 - i):
            for k in range(0, 100 - i - j):
                h = 100 - i - j - k
                a = t[0][0] * i + t[1][0] * j + t[2][0] * k + t[3][0] * h
                b = t[0][1] * i + t[1][1] * j + t[2][1] * k + t[3][1] * h
                c = t[0][2] * i + t[1][2] * j + t[2][2] * k + t[3][2] * h
                d = t[0][3] * i + t[1][3] * j + t[2][3] * k + t[3][3] * h
                e = t[0][4] * i + t[1][4] * j + t[2][4] * k + t[3][4] * h

                if a <= 0 or b <= 0 or c <= 0 or d <= 0:
                    score = 0
                else:
                    score = a * b * c * d

                if e != 500:
                    score = 0

                if score > max_score:
                    max_score = score


    return max_score



def wow():
    return {'Sue ' + re.match(r'Sue (\d+): (.+?)$', line).groups()[0]: {item.split(': ')[0]: int(item.split(': ')[1]) for item in re.match(r'Sue (\d+): (.+?)$', line).groups()[1].split(', ')} for line in functions.clear_input('input.txt')}

def wow_classique():
    data = functions.clear_input("input.txt")

    sue_data = {}

    # Utiliser une expression régulière pour extraire les données
    pattern = r'Sue (\d+): (.+?)$'

    for line in data:
        match = re.match(pattern, line)
        if match:
            sue_number, sue_info = match.groups()
            sue_info = sue_info.split(', ')
            sue_attributes = {}
            for item in sue_info:
                attribute, value = item.split(': ')
                sue_attributes[attribute] = int(value)
            sue_data[f'Sue {sue_number}'] = sue_attributes

    return sue_data


def ex16():
    signature = {'children': 3,
                 'cats': 7,
                 'samoyeds': 2,
                 'pomeranians': 3,
                 'akitas': 0,
                 'vizslas': 0,
                 'goldfish': 5,
                 'trees': 3,
                 'cars': 2,
                 'perfumes': 1
                 }
    tab = wow()
    for key, value in tab.items():
        cpt = 0
        for element, number in value.items():
            if element in signature.keys():
                if element in ['cats', 'trees']:
                    if signature[element] < number:
                        cpt += 1
                    else:
                        cpt = -1

                elif element in ['pomeranians', 'goldfish']:
                    if signature[element] > number:
                        cpt += 1
                    else:
                        cpt = -1

                elif signature[element] == number:
                    cpt += 1
                else:
                    cpt = -1
        if cpt == 3:
            return key


def ex17():
    conteneurs = functions.clear_input("input.txt")
    conteneurs = [int(x) for x in conteneurs]
    resultats = []
    for r in range(1, len(conteneurs) + 1):
        for combo in combinations(conteneurs, r):
            if sum(list(combo)) == 150:
                resultats.append(list(combo))
    return len(resultats)


def ex17p2():
    conteneurs = functions.clear_input("input.txt")
    conteneurs = [int(x) for x in conteneurs]
    resultats = []
    for r in range(1, len(conteneurs) + 1):
        for combo in combinations(conteneurs, r):
            if sum(list(combo)) == 150:
                resultats.append(list(combo))
    return min([len(x) for x in resultats])


def ex18():
    grille = functions.clear_input("input.txt")
    taille = len(grille)
    t_2 = len(grille[0])
    steps = 0
    tab = []
    grille[0] = '#' + grille[0][1:-1] + '#'
    grille[taille - 1] = '#' + grille[taille - 1][1:-1] + '#'

    while steps != 100:
        for line_idx in range(taille):
            line = []
            for string_idx in range(t_2):
                neighbors = functions.neighbors(grille, string_idx, line_idx)

                if grille[line_idx][string_idx] == '.' and neighbors.count("#") == 3:
                    line.append('#')
                elif grille[line_idx][string_idx] == '#' and (neighbors.count('#') == 2 or neighbors.count("#") == 3):
                    line.append('#')
                else:
                    line.append('.')
            if line_idx == 0:
                line[0] = '#'
                line[-1] = '#'
            elif line_idx == taille - 1:
                line[0] = '#'
                line[-1] = '#'



            tab.append(line)


        grille = tab
        tab = []
        steps += 1
    cpt = 0
    for x in grille:
        cpt += x.count('#')

    return cpt



def ex19():
    possibilities = []
    molecules = functions.clear_input('input.txt', spliter=" => ")
    string = list(molecules[-1].copy()[0])
    molecules = molecules[:-1]
    length = len(string)
    dicto = {key:[] for key in set([x[0] for x in molecules])}

    for key, value in molecules:
        dicto[key].append(value)

    for key, value in dicto.items():
        for index, car in enumerate(string):
            if car == key:
                for multi in value:
                    temp = string.copy()
                    temp[index] = multi
                    possibilities.append(''.join(temp))
            if index != length - 1 and string[index: index + 2] == list(key):
                for multi in value:
                    temp = string.copy()
                    temp[index] = multi
                    temp[index + 1] = ''
                    possibilities.append(''.join(temp))

    return len(set(possibilities))


def part2(replacements: List[List[str]], molecule: str) -> int: # Tout simplemement stratosphérique
    original_replacements = replacements.copy()

    steps = 0
    current_molecule = molecule

    while current_molecule != 'e':
        try:
            replacement = max(replacements, key=lambda x: len(x[1]))
        except ValueError:
            replacements = original_replacements.copy()
            replacement = max(replacements, key=lambda x: len(x[1]))
        before, after = replacement
        new_molecule = current_molecule.replace(after, before, 1)
        if current_molecule != new_molecule:
            steps += 1
        else:
            replacements.remove(replacement)
        current_molecule = new_molecule
    return steps

print(part2([(i, j) for i, j in functions.clear_input("input.txt", spliter=" => ")], "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"))