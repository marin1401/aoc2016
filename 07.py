#Day 07

with open('./07.txt') as myinput:
    inputlines = myinput.readlines()

ip_addresses = [line.replace('[', ']').split(']') for line in inputlines]

#Part 1

counter = 0
for ip_address in ip_addresses:
    condition = set()
    for part in ip_address:
        for a, b, c, d in zip(part, part[1:], part[2:], part[3:]):
            if a == d and b == c and a != b:
                if ip_address.index(part) % 2 == 0:
                    condition.add(True)
                else:
                    condition.add(False)
    counter += condition == {True}

print(counter)

#Part 2

counter = 0
for ip_address in ip_addresses:
    supernet, hypernet = set(), set()
    for part in ip_address:
        for a, b, c in zip(part, part[1:], part[2:]):
            if a == c and a != b:
                if ip_address.index(part) % 2 == 0:
                    supernet.add(a + b + c)
                else:
                    hypernet.add(a + b + c)
    counter += any(aba for aba in supernet if aba[1]+aba[0]+aba[1] in hypernet)

print(counter)
