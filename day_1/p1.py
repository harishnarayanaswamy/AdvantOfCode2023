"""AoC Program 1 - 1a"""
import re

s = 0
text = open("input.txt")
for line in text.readlines():
    l = re.findall('\d+', line )
    f = l[0]
    l = l[-1]
    c = f[0] + l[-1]
    s += int(c)

print(s)