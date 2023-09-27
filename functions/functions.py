import requests
import json
def clear_input(path, spliter=None):
    with open(path, 'r') as fichier:
        tab = fichier.readlines()
    if spliter:
        for i in range(len(tab)):
            tab[i] = tab[i][:-1].split(spliter)
    else:
        for i in range(len(tab)):
            tab[i] = tab[i][:-1]

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

