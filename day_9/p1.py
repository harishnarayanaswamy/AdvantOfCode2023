"""AoC Program 9 - 1a"""

import sys

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")

def get_next_num(line):
    """Next number in the list."""
    num = list(map(int, line.split()))
    next_num = 0
    last_num = []
    while num:
        i = 0
        new_num = []
        while len(num)-1 > i:
            diff = num[i+1]-num[i]
            new_num.append(diff)
            i += 1
        last_num.append(num[-1])
        if all(y==0 for y in new_num):
            num = []
        else:
            num = new_num
    return sum(last_num)

s = 0
for line in lines:
    s += get_next_num(line)
print(s)