#Day 10

with open('./10.txt') as my_input:
    input_lines = my_input.read().splitlines()

def dict_update(d, k, v):
    if k in d.keys():
        d[k].append(v)
    else:
        d[k] = [v]

bots = {}
instructions = []
for line in input_lines:
    if line.split()[0] == 'value':
        value, bot = line.split()[1::4]
        dict_update(bots, bot, int(value))
    else:
        instructions.append(line.split())

bins = {}
responsible = ''
while instructions:
    i = -1
    for b, bn, g, l, t1, d1, d1n, a, h, t2, d2, d2n in instructions:
        i += 1
        if bn in bots.keys():
            if len(bots[bn]) > 1:
                min_v, max_v = sorted(bots[bn])
                if d1 == 'bot':
                    dict_update(bots, d1n, min_v)
                else:
                    dict_update(bins, d1n, min_v)
                if d2 == 'bot':
                    dict_update(bots, d2n, max_v)
                else:
                    dict_update(bins, d2n, max_v)
                bots[bn] = []
                break
    if not responsible:
        for k, v in bots.items():
            if 61 in v and 17 in v:
                responsible = k
    instructions.pop(i)

#Part 1

print(responsible)

#Part 2

product = 1
for i in range(3):
    product *= next(iter(bins[str(i)]))

print(product)