"""AoC Program 8 - 1b"""
import math
import sys
import json

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")

directions = lines[0]

route_map = {}
start_node = []
dir_number = 0
steps = 0
for line in lines[1:]:
    if line:
        key = line.split("=")[0].strip()
        if key[-1] == 'A':
            start_node.append(key)
        val = line.split("=")[1].strip()[1:-1].split(",")
        route_map.update({key: {'L': val[0].strip(), 'R':val[1].strip()}})


def get_next_node(cur_node):
    """get next_node for all start nodes."""
    d = 0
    steps = 0
    while cur_node[-1] != 'Z':
        steps += 1
        dd = directions[d]
        cur_node = route_map[cur_node][dd]
        d += 1
        if d == len(directions):
            d = 0
    return steps


# while True:
lens = [get_next_node(node) for node in start_node]
print(lens)
ans = math.lcm(*lens)
print(ans)
    