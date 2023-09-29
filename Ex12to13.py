from itertools import permutations
from functions import functions
data = functions.encode_json_open('input.json')
total = 0
total_p2 = 0


def ex10(input):
    global total

    if isinstance(input, int):
        total += input
    elif isinstance(input,list):
        for item in input:
            ex10(item)
    elif isinstance(input,dict):
        for value in input.values():
            ex10(value)
    return total


def ex10p2(input):
    global total

    if isinstance(input, int):
        total += input
    elif isinstance(input, list):
        for item in input:
            ex10p2(item)
    elif isinstance(input, dict):
        if "red" in input.values():
            return 0
        for value in input.values():
            ex10p2(value)
    return total


def make_perms():
    dict = {}
    tab = functions.clear_input('input.txt', ' ',2)
    for line in tab:
        if line[0] not in dict.keys():
            dict[line[0]] = {}
        if line[-1] not in dict[line[0]].keys():
            dict[line[0]][line[-1]] = int(line[3]) if line[2] == "gain" else - int(line[3])
            dict[line[0]]['Bastien'] = 0
    dict['Bastien'] = {key: 0 for key in dict.keys()}
    return dict

def ex13():
    dict = make_perms()
    occurences = list(permutations(dict))
    max_happiness = []
    for line in occurences:
        total = 0
        for i in range(len(line)):
            if i == len(line) - 1:
                total += dict[line[i]][line[i - 1]] + dict[line[i]][line[0]]
            else:
                total += dict[line[i]][line[i - 1]] + dict[line[i]][line[i + 1]]
        max_happiness.append(total)
    return max(max_happiness)

