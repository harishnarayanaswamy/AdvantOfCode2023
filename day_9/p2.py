"""AoC Program 9 - 1b"""

import sys

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")


def get_previous_num(input_list):
    new_list = []
    for i in range(len(input_list)-1):
        new_list.append(input_list[i+1]-input_list[i])
    if all(y==0 for y in input_list):
        return input_list[0]
    else:
        return input_list[0]-get_previous_num(new_list)


ans = 0
for line in lines:
    input_list = [int(x) for x in line.split()]
    ans += get_previous_num(input_list)
print(ans)
