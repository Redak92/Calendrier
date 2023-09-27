from functions import functions
from itertools import permutations
from string import ascii_lowercase


def ex8():

    with open('input.txt', 'r') as fichier:
        tab = [eval(line) for line in fichier]

    all_chars = functions.clear_input("input.txt")
    print(f'sum : {sum([len(line) for line in all_chars]) - sum([len(line) for line in tab])}')

def len_str(line):
    cpt = 4
    for i in range(len(line)):
        if line[i] in ['\\', '\'', '\"'] and i not in [0, len(line) - 1]:
            cpt += 1
    print(cpt)
    return cpt

def ex8p2():
    all_chars = functions.clear_input("input.txt")

    return sum([len(line) + len_str(line) for line in all_chars]) - sum([len(line) for line in all_chars])

# Exercice 9

def make_graph(tab):
    graph = {}
    for line in tab:
        if line[0] not in graph.keys():
            graph[line[0]] = {}
        if line[2] not in graph.keys():
            graph[line[2]] = {}
    return graph
def calculate_path_cost(path, graph):
    cpt = 0
    for i in range(len(path) - 1):
        cpt += graph[path[i]][path[i + 1]]
    return cpt



def ex9():
    tab = functions.clear_input("input.txt", " ")
    graph = make_graph(tab)
    for line in tab:
        graph[line[0]][line[2]] = int(line[-1])
        graph[line[2]][line[0]] = int(line[-1])

    return min([calculate_path_cost(path,graph) for path in permutations(graph.keys())]),max([calculate_path_cost(path,graph) for path in permutations(graph.keys())])


def look_and_say(inpt):
    output = ""
    taille = len(inpt)
    i = 0
    while i < taille:
        cpt = 1
        while True:
            if i < taille - 1 and inpt[i] == inpt[i + 1]:
                cpt += 1
                i += 1
            else:
                break
        output += str(cpt) + inpt[i]
        i += 1

    return output

def ex10():

    inpt = "1113122113"

    for i in range(50):
        inpt = look_and_say(inpt)

    return len(inpt)


def is_straight_by_three(string):
    for i in range(len(string) - 2):
        if string[i:i+3] in ascii_lowercase:
            return True
    return False

def no_letters(string):
    for i in string:
        if i in 'iol':
            return False
    return True


def overlapp(string):
    return True if len([string[i] for i in range(len(string) - 1) if string[i] == string[i + 1] and string[i] not in string[:i]]) > 1 else False



def ex11(string):
    string = functions.increment(string)
    while not all([overlapp(string),no_letters(string), is_straight_by_three(string)]):
        string = functions.increment(string)
    return string

print(ex11('hepxxyzz'))