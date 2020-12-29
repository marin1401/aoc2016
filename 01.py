#Day 01

with open('./01.txt') as myinput:
    instructions = myinput.read().split(', ')

direction = 1j
location = 0 + 0j
visited_locations = set()
visited_locations.add(location)
first_location_visited_twice = ''

for instruction in instructions:
    turn = instruction[0]
    blocks = int(instruction[1:])
    if turn == 'L':
        direction *= 1j
    elif turn == 'R':
        direction *= -1j
    for i in range(blocks):
        location += direction
        if first_location_visited_twice == '':
            if location in visited_locations:
                first_location_visited_twice = location
            else:
                visited_locations.add(location)

def get_distance(location):
    return int(abs(location.real) + abs(location.imag))

#Part 1

print(get_distance(location))

#Part 2

print(get_distance(first_location_visited_twice))
