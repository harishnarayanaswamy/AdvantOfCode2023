"""AoC Program 5 - 1b"""

import sys

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")

input = []
l1 = []
for line in lines:
    if line:
        if ":" in line:
            if line.split(':')[1]:
                input_seeds = [int(i) for i in line.split(':')[1].split()]
        else:
            l1.append(tuple(map(int, line.split())))
    else:
        if l1:
            input.append(l1)
            l1 =[]

if l1:
    input.append(l1)
    l1 = []


def loc_of_seed(seed):
    for m in input:
        for (destination, source, counter) in m:
            if source <= seed < source+counter:
                seed = destination + (seed - source)
                break
    return seed


# generate actual list of seeds.
l = input_seeds
first_seed = l[::2]
last_seed = l[1::2]
seeds_range = list(tuple(zip(first_seed, last_seed)))
seeds = []
final_results = []
for i, j in seeds_range:
    seeds += list(range(i,i+j,1))

for seed in seeds:
    final_results.append(loc_of_seed(seed))

print(min(final_results))
