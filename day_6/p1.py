"""AoC Program 6 - 1a"""

import sys

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")

time_list = [int(i) for i in lines[0].split(":")[1].split() if i!=""]
distance_list = [int(i) for i in lines[1].split(":")[1].split() if i!=""]
time_distance_map = list(zip(time_list, distance_list))

def get_win_prob(ele):
    """Get win prob."""
    time, distance = ele
    i = 1
    while time-i > 0:
        if ((time-i) * i) > distance:
            break
        i += 1
    return len(range(i,time-i+1,1))

total = 1
for ele in time_distance_map:
    win_brob = get_win_prob(ele)
    print(win_brob)
    total = win_brob*total
print(total)