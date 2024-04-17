"""AoC Program 2 - 1b"""
"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
import sys
import re

input_data = open(sys.argv[1]).read().strip()
input_lines = input_data.split("\n")

d = {}
for line in input_lines:
    line_split = line.split(':')
    game_count = re.findall('\d+', line_split[0])
    game_split = re.sub(" ", "", line_split[1]).split(';')
    result = {}
    for each in game_split:
        for ele in each.split(','):
            val_in_str = re.findall('\d+', ele)[0]
            k = re.sub(val_in_str,'',ele)
            v = int(val_in_str)
            if k not in result:
                result.update({k:v})
            elif result[k] < v:
                result[k] = v
    d .update({int(game_count[0]): result})

sum = 0
for key, item in d.items():
    sum += item['red'] * item['green'] * item['blue']

print(sum)
    
