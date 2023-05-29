from day1 import Day1
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()
current_day_number_max = 1


def user_input():
    day = input('Enter day number: ')
    if not day or int(day) > current_day_number_max:
        print(f'{Fore.RED}Current maximum day number is {current_day_number_max}{Style.RESET_ALL}')
        print('')
        user_input()
    else:
        part = input('Enter 1 or 2 for part number: ')
        execute_day(day, part)


def execute_day(day, part):
    if int(part) == 1 or int(part) == 2:
        print(f'Executing part {part} of day {day}')
        day1 = Day1(part)
        print('')
        user_input()
    else:
        print((f'{Fore.RED}{part} is not a valid number for part, choose either 1 or 2..{Style.RESET_ALL}'))
        print('')
        user_input()


user_input()
