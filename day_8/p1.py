"""AoC Program 8 - 1a"""
import sys
import json

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")

directions = lines[0]

route_map = {}
for line in lines[1:]:
    if line:
        key = line.split("=")[0].strip()
        val = line.split("=")[1].strip()[1:-1].split(",")
        route_map.update({key: {'L': val[0].strip(), 'R':val[1].strip()}})

nxt_node = 'AAA'
is_final = True
steps = 0
def get_destination():
    global nxt_node, is_final, steps
    for d in directions:
        steps += 1
        nxt_node = route_map[nxt_node][d]
        if nxt_node == 'ZZZ':
            is_final = False
    return is_final 

# while not is_final_node:
while is_final:
    is_final = get_destination()

if nxt_node=='ZZZ':
    print("find the destination")
    print(nxt_node)
    print(steps)