from functions import functions
# Exercice 5

def ex5():
    cpt = 0
    forbidden_strings = ['ab', 'cd', 'pq', 'xy']
    vowels = ['a', 'e', 'i', 'o', 'u']
    with open("input.txt",'r') as fichier:
        tab = fichier.readlines()


    for i in tab:
        red_flag = 0
        same_count = 0
        vowels_count = 0
        for x in range(1,len(i)):
            if i[x - 1] + i[x] in forbidden_strings:
                red_flag = 1

                break
            elif i[x - 1] == i[x]:
                same_count = 1


            if i[x - 1] in vowels:

                vowels_count += 1
        if not red_flag and same_count == 1 and vowels_count > 2:
            cpt += 1

    return cpt


def ex5part2():
    cpt = 0
    with open("input.txt", 'r') as fichier:
        tab = fichier.readlines()



    for i in tab:
        one_one = 0
        two_two = 0
        strings = []
        t = len(i)
        for x in range(1,t - 1):
            if one_one == 0 and i[x - 1] == i[x + 1]:
                one_one = 1

            strings.append(i[x - 1] + i[x])

        for y in range(len(strings)):
            for k in range(y + 2, len(strings)):
                if strings[y] == strings[k]:
                    two_two = 1
                    break

            if two_two == 1:
                break

        if one_one == 1 and two_two == 1:
            cpt += 1

    return cpt





# Exercice 6
def print_matrix(matrix):
    for i in matrix:
        print(i)
def ex6():
    with open("input.txt", 'r') as fichier:
        tab = fichier.readlines()

    lights = [[0 for i in range(0, 1000)] for x in range(0, 1000)]
    taille = len(tab)

    for i in range(taille):
        tab[i] = tab[i][:-1]

    for i in range(taille):
        tab[i] = tab[i].split(" ")
        if tab[i][0] == "toggle":
            t = 4
            first_data = tab[i][1].split(',')
            second_data = tab[i][t - 1].split(',')

            for ab_y in range(int(first_data[1]),int(second_data[1]) + 1):
                for ab_x in range(int(first_data[0]), int(second_data[0]) + 1):
                    lights[ab_x][ab_y] = 1 if lights[ab_x][ab_y] == 0 else 0



        else:

            t = 5
            first_data = tab[i][2].split(',')
            second_data = tab[i][t - 1].split(',')

            if tab[i][1] == "on":
                change = 1
            else:
                change = 0



            for ab_y in range(int(first_data[1]),int(second_data[1]) + 1):
                for ab_x in range(int(first_data[0]), int(second_data[0]) + 1):
                    lights[ab_x][ab_y] = change
    return count_lights(lights)
def count_lights(lights):
    cpt = 0
    for i in lights:
        for x in i:
            if x == 1:
                cpt += 1
    return cpt


def ex6part2():
    with open("input.txt", 'r') as fichier:
        tab = fichier.readlines()

    lights = [[0 for i in range(0, 1000)] for x in range(0, 1000)]
    taille = len(tab)

    for i in range(taille):
        tab[i] = tab[i][:-1]

    for i in range(taille):
        tab[i] = tab[i].split(" ")
        if tab[i][0] == "toggle":
            t = 4
            first_data = tab[i][1].split(',')
            second_data = tab[i][t - 1].split(',')

            for ab_y in range(int(first_data[1]),int(second_data[1]) + 1):
                for ab_x in range(int(first_data[0]), int(second_data[0]) + 1):
                    lights[ab_x][ab_y] += 2



        else:

            t = 5
            first_data = tab[i][2].split(',')
            second_data = tab[i][t - 1].split(',')

            if tab[i][1] == "on":
                change = 1
            else:
                change = -1




            for ab_y in range(int(first_data[1]),int(second_data[1]) + 1):
                for ab_x in range(int(first_data[0]), int(second_data[0]) + 1):
                    lights[ab_x][ab_y] += change
                    if lights[ab_x][ab_y] < 0:
                        lights[ab_x][ab_y] = 0

    return count_lights_p2(lights)

def count_lights_p2(lights):
    cpt = 0
    for i in lights:
        for x in i:
            cpt += x
    return cpt




#Exercice 7

def bin_to_dec(binaire):
    decimal = 0
    puissance = 0
    for bit in reversed(binaire):
        if bit == '1':
            decimal += 2 ** puissance
        puissance += 1

    return decimal

def dec_to_bin(decimal):
    if decimal == 0:
        return "0"

    binaire = ""

    while decimal > 0:
        bit = decimal % 2
        binaire = str(bit) + binaire
        decimal //= 2

    return binaire


def and_door(in1, in2):
    res = 0

    min_len = min(len(in1),len(in2))
    in2 = in2[-min_len:]
    in1 = in1[-min_len:]
    power = min_len - 1

    for i in range(min_len):
        if in2[i] == "1" and in1[i] == "1":
            res += 2**power
        power -= 1
    return res


def or_door(in1, in2):
    res = 0

    if len(in1) > len(in2):
        max_len = len(in1)

        while len(in2) < max_len:
            in2 = "0" + in2
    else:
        max_len = len(in2)
        while len(in1) != max_len:
            in1 = "0" + in1
    power = max_len - 1

    for i in range(0,max_len):
        if in1[i] == "1" or in2[i] == "1":
            res += 2 ** power
        power -= 1
    return res


def not_door(in1): # Fonction pompée, à mieux comprendre même si c'est simple
    if len(in1) > 16:
        raise ValueError("L'entrée ne doit pas dépasser 16 bits.")
    elif len(in1) < 16:
        in1 = '0' * (16 - len(in1)) + in1

    inverted = ''.join(['0' if bit == '1' else '1' for bit in in1])
    return int(inverted, 2)


def shift(in1, nb, direction):

    if direction == "l":
        for i in range(nb):
            in1 = in1 + "0"
    else:
        in1 = in1[:-nb]

    return bin_to_dec(in1)

def del_elements(tab,tab2):
    for i in tab2:
        tab.remove(i)

def base_wires():
    wires = {}
    tab = functions.clear_input("input.txt", " ")
    to_delete = []

    for line in tab:
        if line[1] == "->" and line[0].isdigit():
            wires[line[2]] = int(line[0])
            to_delete.append(line)
        elif line[2] == "->" and line[1].isdigit():
            wires[line[3]] = not_door(dec_to_bin(int(line[1])))
            to_delete.append(line)
        elif line[0].isdigit() and line[2].isdigit():
            if line[1] == "AND":
                wires[line[4]] = and_door(dec_to_bin(int(line[0])),dec_to_bin(int(line[2])))
            elif line[1] == "OR":
                wires[line[4]] = or_door(dec_to_bin(int(line[0])),dec_to_bin(int(line[2])))

            else:
                if line[1][0] == "L":
                    wires[line[4]] = shift(dec_to_bin(int(line[0])), int(line[2]),'l')
                else:
                    wires[line[4]] = shift(dec_to_bin(int(line[0])), int(line[2]), 'r')
            to_delete.append(line)

    del_elements(tab,to_delete)
    return wires,tab

def osint(nb):
    return isinstance(nb,int)

def ex7():
    f = base_wires()
    wires = f[0]
    tab = f[1]
    cpt = 0
    for line in tab:
        wires[line[-1]] = line[:-2]
    for i in range(16):
        wires[str(i)] = i

    while not osint(wires['a']):
        for line in tab:
            if osint(wires[line[-1]]):
                continue
            elif "AND" in line and osint(wires[line[0]]) and osint(wires[line[2]]):
                wires[line[-1]] = wires[line[0]] & wires[line[2]]
            elif "OR" in line and osint(wires[line[0]]) and osint(wires[line[2]]):
                wires[line[-1]] = wires[line[0]] | wires[line[2]]
            elif "NOT" in line and osint(wires[line[1]]):
                wires[line[-1]] = ~wires[line[1]] & 0xFFFF
            elif "LSHIFT" in line and osint(wires[line[0]]) and osint(wires[line[2]]):
                wires[line[-1]] =   (wires[line[0]] << wires[line[2]]) & 0xFFFF
            elif "RSHIFT" in line and osint(wires[line[0]]) and osint(wires[line[2]]):
                wires[line[-1]] =   (wires[line[0]] >> wires[line[2]]) & 0xFFFF
            elif len(line) == 3 and osint(wires[line[0]]):
                wires[line[-1]] = wires[line[0]]
    return wires['a']

print(ex7())
