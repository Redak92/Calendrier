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


