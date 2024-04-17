"""AoC Program 21 - 1a"""

import sys

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")

rows = cols = len(lines)
a = []
start_row = 0
start_cols = 0
for i, line in enumerate(lines):
    b = []
    for j, c in enumerate(line):
        if c == ".":
            b.append(1)
        elif c == '#':
            b.append(0)
        elif c == "S":
            start_row = i
            start_cols = j
            b.append(1)
    a.append(b)

def get_posible_gardens(row, col):
    """Get possible gardens"""
    n = []
    if a[row][col+1] == 1 and col+1 < cols:
        if (row, col+1) not in visited_gardens:
            n.append((row, col+1))
    if a[row][col-1] == 1 and col-1>=0:
        if (row, col-1) not in visited_gardens:
            n.append((row, col-1))
        
    if a[row+1][col] == 1 and row+1 < cols:
        if (row+1, col) not in visited_gardens:
            n.append((row+1, col))
        
    if a[row-1][col] == 1 and row-1 >= 0:
        if (row+1, col) not in visited_gardens:
            n.append((row-1, col))
        
    return n


visited_gardens = []
next_gardens = [[(start_row, start_cols)]]
next_step = [[(start_row, start_cols)]]
for k, i in enumerate(next_step):
    next_round = []
    for j in i:
        row, col = j
        visited_gardens.append((row,j))
        next_round.extend(get_posible_gardens(row, col))
    next_step.append(list(set(next_round)))
    if k == 63:
        break
print(len(next_step[-1]))
