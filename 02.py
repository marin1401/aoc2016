#Day 02

with open('./02.txt') as myinput:
    instructions = myinput.readlines()

keypad_1 = {i + 1: (i % 3 - 1, 1 + (i % 3 - i) // 3) for i in range(9)}

keypad_2 = {                              1: (0,  2),
                           2: (-1,  1),   3: (0,  1),   4: (1,  1),
            5: (-2,  0),   6: (-1,  0),   7: (0,  0),   8: (1,  0),   9: (2, 0),
                         'A': (-1, -1), 'B': (0, -1), 'C': (1, -1),
                                        'D': (0, -2)}

def get_key(direction, key, keypad, keypad_len):
    (x, y) = keypad[key]
    if direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    elif direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1
    if keypad_len == 9 and -2 < x < 2 and -2 < y < 2 or keypad_len == 13 and abs(x) + abs(y) < 3:
        key = next(k for k, v in keypad.items() if v == (x, y))
    return key 

def get_code(instructions, keypad, keypad_len):
    code = ''
    key = 5
    for instruction in instructions:
        for direction in instruction:
            key = get_key(direction, key, keypad, keypad_len)
        code += str(key)
    return code

#Part 1

print(get_code(instructions, keypad_1, len(keypad_1)))

#Part 2

print(get_code(instructions, keypad_2, len(keypad_2)))
