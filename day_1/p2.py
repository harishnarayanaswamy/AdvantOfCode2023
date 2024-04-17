"""AoC Program 1 - 1b."""
import re

s = 0
text = open("input.txt")
d = {
    'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
    'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
}
def replace_text(key, text):
    return re.sub(key, d[key], text)

for txt in text.readlines():
    l1 = re.sub('one', 'o1e', txt)
    l2 = re.sub('two', 't2o', l1)
    l3 = re.sub('three', 't3e', l2)
    l4 = re.sub('four', 'f4r', l3)
    l5 = re.sub('five', 'f5e', l4)
    l6 = re.sub('six', 's6x', l5)
    l7 = re.sub('seven', 's7n', l6)
    l8 = re.sub('eight', 'e8t', l7)
    l9 = re.sub('nine', 'n9e', l8)
    
    l = re.findall('\d+', l9)
    f = l[0]
    l = l[-1]
    c = f[0] + l[-1]
    s += int(c)

print(s)
