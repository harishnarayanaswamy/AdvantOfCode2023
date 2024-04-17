"""AoC Program 5 - 1a"""

import sys


txt_data = open(sys.argv[1]).read().strip()

def loc_of_seed(seed):
    for m in input:
        for (destination, source, counter) in m:
            if source <= seed < source+counter:
                seed = destination + (seed - source)
                break
    return seed
    

lines = txt_data.split("\n")
seeds = []
input=[]
l1 = []
for line in lines:
    if line:
        if not ':' in line:
            l1.append(tuple(map(int, line.split())))
        elif line.split(":")[1]:
            seeds = list(map(int, line.split(":")[1].split()))
    elif l1:
        input.append(l1)
        l1 = []
# append last set of input is input list
if l1:
    input.append(l1)
final_results = []

for seed in seeds:
    final_results.append(loc_of_seed(seed))
    
print(min(final_results))
