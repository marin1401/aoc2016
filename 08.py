#Day 08

with open('./08.txt') as myinput:
    inputlines = myinput.readlines()

instructions = [line.strip().replace(' by ', ',').replace('=', ' ').split()[-2:] for line in inputlines]

screen_width = 50
screen_height = 6

screen = [[0 for column in range(screen_width)] for row in range(screen_height)]

#Part 1

for instruction in instructions:
    do, parameter = instruction
    if do == 'rect':
        columns, rows = map(int, parameter.split('x'))
        for row in range(rows):
            for column in range(columns):
                screen[row][column] = 1
    elif do == 'x':
        column, shift = map(int, parameter.split(','))
        column_list = [screen[row][column] for row in range(screen_height)]
        column_list = column_list[-shift:] + column_list[:-shift]
        for row in range(screen_height):
            screen[row][column] = column_list[row]
    elif do == 'y':
        row, shift = map(int, parameter.split(','))
        screen[row] = screen[row][-shift:] + screen[row][:-shift]

print(sum(map(sum, screen)))

#Part 2

for row in range(screen_height):
    for column in range(screen_width):
        screen[row][column] = str(screen[row][column]).replace('0', ' ').replace('1', '#')

code = map(''.join, screen)

for row in code:
    print(row)