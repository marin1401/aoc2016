#Day 09

import math

with open('./09.txt') as my_input:
    compressed_file = my_input.read()

#Part 1

marker = ''
n, repeat = 0, 0
length = 0
for char in compressed_file:
    if n:
        n -= 1
    else:
        marker += char
        if ')' in marker:
            n, repeat = map(int, marker[1:-1].split('x'))
            length += n * repeat
            marker = ''

print(length)

#Part 2

marker = ''
m = False
n, repeat = [], []
length, counter = 0, 0
for char in compressed_file:
    if char in ('(', ')'):
        m = True if char == '(' else False
        n = [i-1 for i in n]
        if char == ')':
            n.append(int(marker.split('x')[0]))
            repeat.append(int(marker.split('x')[1]))
            marker = ''
    elif m:
        marker += char
        n = [i-1 for i in n]
    else:
        counter += 1
        if n[-1] == 1:
            length += counter * math.prod(repeat)
            counter = 0
        n = [i-1 for i in n]
        while n:
            if not n[-1]:
                n.pop()
                repeat.pop()
            else:
                break

print(length)