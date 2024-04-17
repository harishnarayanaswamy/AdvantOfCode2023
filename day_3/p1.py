"""AoC Program 3 - 1a"""
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
*12.......
"""

import sys

input_text = open(sys.argv[1]).read().strip()
txt_lines = input_text.split('\n')

last_line_index = len(txt_lines) - 1
number_str = ''
total = 0
is_engine_part = False
for index, line in enumerate(txt_lines):
    line_length = len(line) - 1
    for j, txt in enumerate(line) :
        if txt.isnumeric():
            if index == 0:
                if j == 0:
                    if (txt_lines[index+1][j] != "." and not txt_lines[index+1][j].isdigit()) or \
                        (txt_lines[index+1][j+1] != "." and not txt_lines[index+1][j+1].isdigit()):
                        
                        is_engine_part = True
                elif j == line_length:
                    if (txt_lines[index+1][j-1] != "." and not txt_lines[index+1][j-1].isdigit()) or \
                        (txt_lines[index+1][j] != "." and not txt_lines[index+1][j].isdigit()):
                        
                        is_engine_part = True
                else:
                    if (txt_lines[index+1][j-1] != "." and not txt_lines[index+1][j-1].isdigit()) or \
                        (txt_lines[index+1][j] != "." and not txt_lines[index+1][j].isdigit()) or \
                        (txt_lines[index+1][j+1] != "." and not txt_lines[index+1][j+1].isdigit()):
                        
                        is_engine_part = True
            elif index == last_line_index:
                if j==0:
                    if (txt_lines[index-1][j] != "." and not txt_lines[index-1][j].isdigit()) or \
                        (txt_lines[index-1][j+1] != "." and not txt_lines[index-1][j+1].isdigit()):
                        
                        is_engine_part = True
                elif j == line_length:
                    if (txt_lines[index-1][j-1] != "." and not txt_lines[index-1][j-1].isdigit()) or \
                        (txt_lines[index-1][j] != "." and not txt_lines[index-1][j].isdigit()):
                        
                        is_engine_part = True
                else:
                    if (txt_lines[index-1][j-1] != "." and not txt_lines[index-1][j-1].isdigit()) or \
                        (txt_lines[index-1][j] != "." and not txt_lines[index-1][j].isdigit()) or \
                        (txt_lines[index-1][j+1] != "." and not txt_lines[index-1][j+1].isdigit()):
                        
                        is_engine_part = True
            else:
                if j==0:
                    if (txt_lines[index+1][j] != "." and not txt_lines[index+1][j].isdigit()) or \
                        (txt_lines[index+1][j+1] != "." and not txt_lines[index+1][j+1].isdigit()) or \
                        (txt_lines[index-1][j+1] != "." and not txt_lines[index-1][j+1].isdigit()) or \
                        (txt_lines[index-1][j] != "." and not txt_lines[index-1][j].isdigit()):\
                        
                        is_engine_part = True
                elif j == line_length:
                    if (txt_lines[index+1][j] != "." and not txt_lines[index+1][j].isdigit()) or \
                        (txt_lines[index+1][j-1] != "." and not txt_lines[index+1][j-1].isdigit()) or \
                        (txt_lines[index-1][j] != "." and not txt_lines[index-1][j].isdigit()) or \
                        (txt_lines[index-1][j-1] != "." and not txt_lines[index-1][j-1].isdigit()):
                        
                        is_engine_part = True
                else:
                    
                    if (txt_lines[index+1][j] != "." and not txt_lines[index+1][j].isdigit()) or \
                        (txt_lines[index+1][j+1] != "." and not txt_lines[index+1][j+1].isdigit()) or \
                        (txt_lines[index+1][j-1] != "." and not txt_lines[index+1][j-1].isdigit()) or \
                        (txt_lines[index-1][j+1] != "." and not txt_lines[index-1][j+1].isdigit()) or \
                        (txt_lines[index-1][j] != "." and not txt_lines[index-1][j].isdigit()) or \
                        (txt_lines[index-1][j-1] != "." and not txt_lines[index-1][j-1].isdigit()):
                        
                        is_engine_part = True
            number_str += txt
        else:
            if is_engine_part:
                total += int(number_str)
                number_str = ""
            elif txt != ".":
                if number_str:
                    total += int(number_str)
                    number_str = ""
            elif number_str:
                if line[j-(len(number_str)+1)] != ".":
                    total += int(number_str)
            number_str = ''
            is_engine_part = False
print(total)
