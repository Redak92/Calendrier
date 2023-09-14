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

print(ex5())


