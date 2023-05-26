from day1 import Day1


def user_input():
    day = input('Enter day number: ')
    part = input('Enter 1 or 2 for part number: ')
    execute_day(day, part)


def execute_day(day, part):
    if int(part) == 1 or int(part) == 2:
        print(f'Executing part {part} of day {day}')
        day1 = Day1(part)
        print('')
        user_input()
    else:
        print(f'{part} is not a valid number for part, choose either 1 or 2..')
        user_input()


user_input()
