#Day 01

with open('./01.txt') as myinput:
    instructions = myinput.read().split(', ')

#Part 1

direction = 'N'
x = 0
y = 0
path = [] #for part 2
for instruction in instructions:
    steps = int(instruction[1:])
    if instruction[0] == 'L':
        if direction == 'N':
            for i in range(steps):
                path.append((x-i, y))
            x -= steps
            direction = 'W'
        elif direction == 'S':
            for i in range(steps):
                path.append((x+i, y))
            x += steps
            direction = 'E'
        elif direction == 'W':
            for i in range(steps):
                path.append((x, y-i))
            y -= steps
            direction = 'S'
        elif direction == 'E':
            for i in range(steps):
                path.append((x, y+i))
            y += steps
            direction = 'N'
    else:
        if direction == 'N':
            for i in range(steps):
                path.append((x+i, y))
            x += steps
            direction = 'E'
        elif direction == 'S':
            for i in range(steps):
                path.append((x-i, y))
            x -= steps
            direction = 'W'
        elif direction == 'W':
            for i in range(steps):
                path.append((x, y+i))
            y += steps
            direction = 'N'
        elif direction == 'E':
            for i in range(steps):
                path.append((x, y-i))
            y -= steps
            direction = 'S'

print(abs(x) + abs(y))

#Part 2

path_set = set()
for step_coords in path:
    if step_coords in path_set:
        print(abs(step_coords[0]) + abs(step_coords[1]))
        break
    else:
        path_set.add(step_coords)
