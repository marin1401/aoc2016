#Day 02

with open('./02.txt') as myinput:
    instructions = myinput.readlines()

#Part 1

code = ''
key = 5
for instruction in instructions:
    for direction in instruction:
        if key == 1:
            if direction == 'D':
                key = 4
            elif direction == 'R':
                key = 2
        elif key == 2:
            if direction == 'D':
                key = 5
            elif direction == 'L':
                key = 1
            elif direction == 'R':
                key = 3
        elif key == 3:
            if direction == 'D':
                key = 6
            elif direction == 'L':
                key = 2
        elif key == 4:
            if direction == 'U':
                key = 1
            elif direction == 'D':
                key = 7
            elif direction == 'R':
                key = 5
        elif key == 5:
            if direction == 'U':
                key = 2
            elif direction == 'D':
                key = 8
            elif direction == 'L':
                key = 4
            elif direction == 'R':
                key = 6
        elif key == 6:
            if direction == 'U':
                key = 3
            elif direction == 'D':
                key = 9
            elif direction == 'L':
                key = 5
        elif key == 7:
            if direction == 'U':
                key = 4
            elif direction == 'R':
                key = 8
        elif key == 8:
            if direction == 'U':
                key = 5
            elif direction == 'L':
                key = 7
            elif direction == 'R':
                key = 9
        else:
            if direction == 'U':
                key = 6
            elif direction == 'L':
                key = 8
    code += str(key)

print(code)

#Part 2

code = ''
for instruction in instructions:
    for direction in instruction:
        if key == 1:
            if direction == 'D':
                key = 3
        elif key == 2:
            if direction == 'D':
                key = 6
            elif direction == 'R':
                key = 3
        elif key == 3:
            if direction == 'U':
                key = 1
            elif direction == 'D':
                key = 7
            elif direction == 'L':
                key = 2
            elif direction == 'R':
                key = 4
        elif key == 4:
            if direction == 'D':
                key = 8
            elif direction == 'L':
                key = 3
        elif key == 5:
            if direction == 'R':
                key = 6
        elif key == 6:
            if direction == 'U':
                key = 2
            elif direction == 'D':
                key = 'A'
            elif direction == 'L':
                key = 5
            elif direction == 'R':
                key = 7
        elif key == 7:
            if direction == 'U':
                key = 3
            elif direction == 'D':
                key = 'B'
            elif direction == 'L':
                key = 6
            elif direction == 'R':
                key = 8
        elif key == 8:
            if direction == 'U':
                key = 4
            elif direction == 'D':
                key = 'C'
            elif direction == 'L':
                key = 7
            elif direction == 'R':
                key = 9
        elif key == 9:
            if direction == 'L':
                key = 8
        elif key == 'A':
            if direction == 'U':
                key = 6
            elif direction == 'R':
                key = 'B'
        elif key == 'B':
            if direction == 'U':
                key = 7
            elif direction == 'D':
                key = 'D'
            elif direction == 'L':
                key = 'A'
            elif direction == 'R':
                key = 'C'
        elif key == 'C':
            if direction == 'U':
                key = 8
            elif direction == 'L':
                key = 'B'
        else:
            if direction == 'U':
                key = 'B'
    code += str(key)

print(code)