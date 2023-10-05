from functions import functions
import re
from itertools import combinations


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
