#Day 06

with open('./06.txt') as myinput:
    messages = myinput.readlines()

all_letters = [[message[letter_position] for message in messages] for letter_position in range(len(messages[-1]))]
letters_freq = [[(letters.count(letter), letter) for letter in set(letters)] for letters in all_letters]

#Part 1

print(''.join([max(letters)[1] for letters in letters_freq]))

#Part 2

print(''.join([min(letters)[1] for letters in letters_freq]))
