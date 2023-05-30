from day1 import Day1
from day2 import Day2
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()
current_day_number_max = 2


def user_input():
    day = input('Enter day number: ')
    if not day or int(day) > current_day_number_max:
        print(f'{Fore.RED}Current maximum day number is {current_day_number_max}{Style.RESET_ALL}')
        print('')
        user_input()
    else:
        part = input('Enter 1 or 2 for part number: ')
        execute_part(day, part)


def execute_part(day, part):
    if int(part) == 1 or int(part) == 2:
        print(f'Executing day {day}, part {part}')
        execute_day_and_part(int(day), int(part))
        print('')
        user_input()
    else:
        print(f'{Fore.RED}{part} is not a valid number for part, choose either 1 or 2..{Style.RESET_ALL}')
        print('')
        user_input()


def execute_day_and_part(day, part):
    match day:
        case 1:
            day1 = Day1(part)
        case 2:
            day2 = Day2(part)


user_input()