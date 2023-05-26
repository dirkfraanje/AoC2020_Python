def part1():
    input_part1 = []
    # enter your puzzle input in day1.txt
    with open('day1.txt') as f:
        for line in f:
            input_part1.append(int(line))
    desired_result = 2020
    # loop trough the values
    for value in list(input_part1):
        # the current value can now be removed from the original input, this has 2 advantages:
        # a. it will not be checked against itself
        # b. if no match is found and we remove it the input list will get shorter with each iteration, thus improving performance
        input_part1.remove(value)
        if result_found(value, input_part1, desired_result):
            break


def result_found(working_value, list, desired_result):
    for value in list:
        if (working_value + value) == desired_result:
            print(f'Result: {working_value * value} ({working_value} * {value})')
            return True
    return False


def part2():
    pass


class Day1:
    def __init__(self, part):
        if int(part) == 1:
            part1()
        if int(part) == 2:
            part2()
