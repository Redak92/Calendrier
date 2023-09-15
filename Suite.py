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


print(ex6part2())