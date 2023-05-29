from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def part1():
    input_part1 = []
    # enter your puzzle input in day1.txt
    with open('day1.txt') as input_1:
        for line in input_1:
            input_part1.append(int(line))
    desired_result = 2020
    # loop through the values
    for value in list(input_part1):
        # the current value can now be removed from the original input, this has 2 advantages: a. it will not be
        # checked against itself b. if no match is found, and we remove it, the input list will get shorter with each
        # iteration, thus improving performance
        input_part1.remove(value)
        if result_found(value, input_part1, desired_result):
            break


def result_found(working_value, list, desired_result):
    for value in list:
        if (working_value + value) == desired_result:
            print(f'Result: {Fore.GREEN}{working_value * value}{Style.RESET_ALL} ({working_value} * {value})')
            return True
    return False


def part2():
    input_part2 = []
    # enter your puzzle input in day1.txt
    with open('day1.txt') as input:
        for line in input:
            input_part2.append(int(line))
    desired_result = 2020
    # loop through the values
    for value in list(input_part2):
        # the current value can now be removed from the original input, this has 2 advantages: a. it will not be
        # checked against itself b. if no match is found, and we remove it, the input list will get shorter with each
        # iteration, thus improving performance
        input_part2.remove(value)
        if result_found_2(value, list(input_part2), desired_result):
            break


def result_found_2(working_value, input_level_2, desired_result):
    for value in list(input_level_2):
        input_level_2.remove(value)
        result_test = result_found_3(value,input_level_2, desired_result-working_value)
        if result_test:
            result_value = desired_result - working_value - value
            print(f'Result: {Fore.GREEN}{working_value * value * result_value}{Style.RESET_ALL} ({working_value} * {value} * {result_value})')
            return True
    return False


def result_found_3(working_value, input_level_3, desired_result):
    for value in input_level_3:
        if (working_value + value) == desired_result:
            return True
    return False

class Day1:
    def __init__(self, part):
        if int(part) == 1:
            part1()
        if int(part) == 2:
            part2()
