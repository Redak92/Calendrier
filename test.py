def nooverlap(string):
    for i in range(len(string)-1):
        double = string[i:i+2]
        lereste = string[i+2:]
        if double in lereste:
            return True

    return False

def oneletterbetween(string):
    liste1 = []
    for i in range(2,len(string)):
        liste1.append(string[i-2]+string[i-1]+string[i])
    double = 0
    for x in liste1:
        if x[0] == x[2]:
            double += 1
    if double >= 1:
        return True
    else:
        return False

oneletterbetween("abcded")

file = open("input.txt","r")
words = file.readlines()
liste2 = []
for i in words:
    i = i[:-1]
    liste2.append(i)

def goodornot(string):
    nicewords = 0
    for i in string:
        if (nooverlap(i) == True) and (oneletterbetween(i) == True):
            nicewords += 1
    return nicewords
goodornot(liste2)