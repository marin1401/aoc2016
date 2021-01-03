#Day 04

with open('./04.txt') as myinput:
    inputlines = myinput.readlines()

rooms_list = [i.strip().replace('-', '') for i in inputlines]
rooms = {i[:-10]: (int(i[-10:-7]), i[-6:-1]) for i in rooms_list}

#Part 1

id_sum = 0
real_rooms = {}
for k, v in rooms.items():
    most_common = {char: k.count(char) for char in k}
    sorted_most_common = sorted(most_common, key=lambda k: (-most_common[k], k))
    if v[1] == ''.join(sorted_most_common[:5]):
        id_sum += v[0]
        real_rooms[k] = v

print(id_sum)

#Part 2

for k, v in real_rooms.items():
    decrypted = ''
    for key in k:
        decrypted += chr((ord(key) + v[0] - 97) % 26 + 97)
    if 'northpole' in decrypted:
        print(v[0])
        break
