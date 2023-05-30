from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def part1():
    valid_passwords = 0
    with open('day2.txt') as input_1:
        for line in input_1:
            if password_is_valid(line):
                valid_passwords += 1
    print(f'Number of valid passwords: {Fore.GREEN}{valid_passwords}{Style.RESET_ALL}')

def part2():
    print(f'{Fore.LIGHTRED_EX}Work in progress...{Style.RESET_ALL}')

def password_is_valid(line):
    splitted_line = line.split()
    range_minimum = int(splitted_line[0].split('-')[0])
    range_maximum = int(splitted_line[0].split('-')[1])
    required_character = splitted_line[1][0]
    password = splitted_line[2]
    required_character_occurrences = password.count(required_character)

    return range_minimum <= required_character_occurrences <= range_maximum


class Day2:
    def __init__(self, part):
        if int(part) == 1:
            part1()
        if int(part) == 2:
            part2()
