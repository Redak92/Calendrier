from functions import functions
def ex8():

    with open('input.txt', 'r') as fichier:
        tab = [eval(line) for line in fichier]

    all_chars = functions.clear_input("input.txt")
    print(f'sum : {sum([len(line) for line in all_chars]) - sum([len(line) for line in tab])}')

def ex8p2():
    all_chars = '""'

    print(all_chars)


ex8p2()