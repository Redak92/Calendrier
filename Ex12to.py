import json
from functions import functions
data = functions.encode_json_open('input.json')
total = 0


def ex10(input):
    global total

    if isinstance(input, int):
        total += input
    elif isinstance(input,list):
        for item in input:
            ex10(item)
    elif isinstance(input,dict):
        for value in input.values():
            ex10(value)
    return total
print(ex10(data))