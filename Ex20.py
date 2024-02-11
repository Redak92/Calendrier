from tqdm import tqdm
from sympy import divisors



def ex20(puzzle_input: int = 36000000) -> int:
    house = 1
    while True:
        if sum(divisors(house)) * 10 >= puzzle_input:
            return house
        else:
            house += 1

def ex20part2(puzzle_input: int = 36000000) -> int:
    house = 1
    while True:
        if sum(elf for elf in divisors(house) if elf * 50 >= house) * 11 > puzzle_input:
            return house
        else:
            house += 1

print(ex20part2())
"""# Correction
import pytest
import progressbar
from sympy import divisors


@pytest.mark.parametrize('data, expected', [(130, 8)])
def test_part1(data: int, expected: int):
    assert part1(data) == expected


def calculate_presents(house_number, presents_per_house, limit: int = None) -> int:
    if limit:
        visits = sum(elf for elf in divisors(house_number) if house_number <= elf * limit)
    else:
        visits = sum(divisors(house_number))
    return visits * presents_per_house


def part1(target: int) -> int:
    house_number = 1
    with progressbar.ProgressBar(max_value=776160, redirect_stdout=True) as p:
        while calculate_presents(house_number, 10) < target:
            house_number += 1
            p.update(house_number)
    return house_number


def part2(target: int) -> int:
    house_number = 1
    with progressbar.ProgressBar(max_value=786240, redirect_stdout=True) as p:
        while calculate_presents(house_number, 11, 50) < target:
            house_number += 1
            p.update(house_number)
    return house_number


def main():
    target = 33100000
    print(f'Part 1: {part1(target)}')
    print(f'Part 2: {part2(target)}')


if __name__ == "__main__":
    main()
"""