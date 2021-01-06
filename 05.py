#Day 05

import hashlib

with open('./05.txt') as myinput:
    door_id = myinput.read()

def find_passwords(door_id):
    password_1 = ''
    password_2 = ['' for i in range(8)]
    i = 0
    while '' in password_2:
        md5_hash = hashlib.md5(f'{door_id}{i}'.encode()).hexdigest()
        if md5_hash[:5] == '00000':
            if len(password_1) < 8:
                password_1 += md5_hash[5]
            if md5_hash[5].isdigit():
                position = int(md5_hash[5])
                if position in range(8):
                    if not password_2[position]:
                        password_2[position] = md5_hash[6]
        i += 1
    return password_1, ''.join(password_2)

password_1, password_2 = find_passwords(door_id)

#Part 1

print(password_1)

#Part 2

print(password_2)