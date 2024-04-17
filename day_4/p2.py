"""AoC Program 4 - 1b"""
"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

import sys
import re
from collections import defaultdict

raw_data = open(sys.argv[1]).read().strip()
data_lines = raw_data.split("\n")
sum = 0

d = {}
for line in data_lines:
    line_split = line.split(':')
    card_number = re.findall('\d+', line_split[0])
    k = int(card_number[0])
    d.update({k: [line]})

for k, v in d.items():
    sum += len(v)
    for line in v:
        line_split = line.split(':')
        card_number = re.findall('\d+', line_split[0])
        k = int(card_number[0])
        games_split = line_split[1].split('|')
        winning_numbers = [int(i) for i in games_split[0].split()]
        played_winning_numbers = [int(i) for i in games_split[1].split() if int(i) in winning_numbers]
        for index, ele in enumerate(played_winning_numbers):
            i = k+index+1
            d[i].append(data_lines[i-1])

print(sum)  
