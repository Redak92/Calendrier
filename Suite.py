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


print(ex5part2())


# Exercice 6

def ex6():
    




