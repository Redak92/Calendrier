import json
def clear_input(path, spliter=None,left_marge=1):
    with open(path, 'r') as fichier:
        tab = fichier.readlines()
    if spliter:
        for i in range(len(tab)):
            tab[i] = tab[i][:-left_marge].split(spliter)
    else:
        for i in range(len(tab)):
            tab[i] = tab[i][:-left_marge]

    return tab


def increment(string):
    chars = list(string)
    idx = len(chars) - 1
    while idx >= 0 and chars[idx] == 'z':
        chars[idx] = 'a'
        idx -= 1
    if idx >= 0:
        chars[idx] = chr(ord(chars[idx]) + 1)
    else:
        chars.append('a')

    return ''.join(chars)

def encode_json_open(path):
    with open(path, 'r') as fichier:
        data = json.load(fichier)
    return data


def neighbors(matrix, x_abs, y_ord):
    taille = len(matrix)
    t_2 = len(matrix[0])
    tab = []
    for i in range(-1, 2):
        for x in range(-1, 2):
            if 0 <= y_ord + i < taille and 0 <= x_abs + x < t_2 and (i, x) != (0, 0):
                tab.append(matrix[y_ord + i][x_abs + x])

    return tab




