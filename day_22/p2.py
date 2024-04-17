"""AoC Program 22 - 1b"""

"""AoC Program 22 - 1a"""

import sys
import re

from collections import defaultdict
P = complex


input_txt = open(sys.argv[1]).read().strip()
bricks = [list(map(int, re.findall("-?\d+", l)))+[i] for i,l in enumerate(input_txt.splitlines())]
bricks.sort(key = lambda b:b[2])
sitsOn = defaultdict(set)
children = defaultdict(set)
highestZ = defaultdict(lambda:(0,-1))

def getDependencies(children, n):
	inDeg = defaultdict(int)
	for p, kids in children.items():
		for c in kids:
			inDeg[c]+=1
	dep = -1
	Q = [n]
	while Q:
		i = Q.pop()
		dep += 1
		for c in children[i]:
			inDeg[c]-=1
			if inDeg[c] == 0:
				Q.append(c)
	return dep


for b in bricks:
    x1,y1,z1,x2,y2,z2,ind = b
    nZ = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            nZ = max(nZ, highestZ[P(x,y)][0])
    height = z2 - z1 + 1
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            old = highestZ[P(x,y)]
            if old[0] == nZ:
                sitsOn[ind].add(old[1])
                children[old[1]].add(ind)
            highestZ[P(x,y)] = (nZ + height, ind)

for c in children[-1]:
		del sitsOn[c]
del children[-1]

unsafe = set()
for k,v in sitsOn.items():
    if len(v) == 1:
        unsafe|=v

sum = 0
for b in unsafe:
	sum += getDependencies(children, b)

print(sum)
