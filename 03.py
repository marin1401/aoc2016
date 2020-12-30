#Day 03

with open('./03.txt') as myinput:
    triangles = myinput.readlines()

triangles = [list(map(int, i.split())) for i in triangles]

def get_sum(length, triangle):
    if length < (sum(triangle) - length):
        return 1
    else:
        return 0

#Part 1

counter = 0
check = set()
for triangle in triangles:
    for length in triangle:
        check.add(get_sum(length, triangle))
    if 0 not in check:
        counter += 1
    check = set()

print(counter)

#Part 2

triangles_v = []
for i in range(3):
    for triangle in triangles:
        triangles_v.append(triangle[i])

counter = 0
check = set()
for i in range(0, len(triangles_v) - 2, 3):
    for j in range(3):
        check.add(get_sum(triangles_v[i+j], [triangles_v[i], triangles_v[i+1], triangles_v[i+2]]))
    if 0 not in check:
        counter += 1
    check = set()

print(counter)