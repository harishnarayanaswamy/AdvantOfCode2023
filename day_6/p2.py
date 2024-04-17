"""AoC Program 6 - 1b"""

import sys
import re

input_txt = open(sys.argv[1]).read().strip()
lines = input_txt.split("\n")

time_str = int("".join(re.findall('\d+', lines[0].split(":")[1])))
distance_str = int("".join(re.findall('\d+', lines[1].split(":")[1])))

def get_win_prob(ele):
    """Get win prob."""
    time, distance = ele
    i = 1
    while time-i > 0:
        if ((time-i) * i) > distance:
            break
        i += 1
    return len(range(i,time-i+1,1))

print(get_win_prob((int(time_str), int(distance_str))))

