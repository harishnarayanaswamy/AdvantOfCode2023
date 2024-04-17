"""AoC Program 3 - 1b"""
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
23.*324..*
..*.......
12........
"""
import sys

input_text = open(sys.argv[1]).read().strip()
input_lines = input_text.split("\n")

gare = 0

def edge_case_numbers_two(index, j, line_len):
    number_str_1 = ''
    number_str_2 = ''
    if not input_lines[index][j-1].isnumeric():
        k = j+1
        while k<=line_len and input_lines[index][k].isnumeric():
            number_str_1 += input_lines[index][k]
            k += 1
    else:
        k = j-1
        while k>=0 and input_lines[index][k].isnumeric():
            number_str_1 = input_lines[index][k] + number_str_1
            k -= 1
    if index == 0:
        if not input_lines[index+1][j].isnumeric():
            if input_lines[index+1][j+1].isnumeric():
                k = j+1
                while k<=line_len and input_lines[index+1][k].isnumeric():
                    number_str_2 += input_lines[index+1][k]
                    k +=1
            elif input_lines[index+1][j-1].isnumeric():
                k = j-1
                while k>=0 and input_lines[index+1][k].isnumeric():
                    number_str_2 = input_lines[index+1][k] + number_str_2
                    k -= 1
        else:
            k = j
            l = j-1
            while k <= line_len and input_lines[index-1][k].isnumeric():
                number_str_2 += input_lines[index-1][k]
                k += 1
            while l >= 0 and input_lines[index-1][l].isnumeric():
                number_str_2 = input_lines[index-1][l] + number_str_2
                l -= 1
    else:
        if not input_lines[index+1][j].isnumeric():
            if input_lines[index+1][j+1].isnumeric():
                k = j+1
                while k<=line_len and input_lines[index+1][k].isnumeric():
                    number_str_2 += input_lines[index+1][k]
                    k +=1
            elif input_lines[index+1][j-1].isnumeric():
                k = j-1
                while k>=0 and input_lines[index+1][k].isnumeric():
                    number_str_2 = input_lines[index+1][k] + number_str_2
                    k -= 1
        if not input_lines[index-1][j].isnumeric():
            if input_lines[index-1][j+1].isnumeric():
                k = j+1
                while k<=line_len and input_lines[index-1][k].isnumeric():
                    number_str_2 += input_lines[index-1][k]
                    k +=1
            elif input_lines[index-1][j-1].isnumeric():
                k = j-1
                while k>=0 and input_lines[index-1][k].isnumeric():
                    number_str_2 = input_lines[index-1][k] + number_str_2
                    k -= 1
        else:
            k = j
            l = j-1
            while k <= line_len and input_lines[index-1][k].isnumeric():
                number_str_2 += input_lines[index-1][k]
                k += 1
            while l >= 0 and input_lines[index-1][l].isnumeric():
                number_str_2 = input_lines[index-1][l] + number_str_2
                l -= 1
    return int(number_str_1) * int(number_str_2)        
                

def new_flow(index, j, line_len):
    number_str_1 = ''
    number_str_2 = ''
    k = j+1
    while k<=line_len and input_lines[index][k].isnumeric():
        number_str_1 += input_lines[index][k]
        k += 1
    l = j-1
    while l>=0 and input_lines[index][l].isnumeric():
        number_str_2 = input_lines[index][l] + number_str_2
        l -= 1
    return int(number_str_1) * int(number_str_2)

def same_line_numaric(index, j, line_len):
    number_str_1 = ''
    number_str_2 = ''
    k = j-1
    l = j+1
    while k>=0 and input_lines[index][k].isnumeric():
        number_str_1 = input_lines[index][k] + number_str_1
        k -= 1
    while l<=line_len and input_lines[index][l].isnumeric():
        number_str_2 += input_lines[index][l]
        l += 1
    return int(number_str_1) * int(number_str_2)
    
def edge_case_last_line(index, j, line_len):
    number_str_1 = ''
    number_str_2 = ''
    if j==0:
        k = j+1
        while j<=line_len and input_lines[index][k].isnumeric():
            number_str_1 += input_lines[index][k]
            k = k+1
        k=j
        if not input_lines[index-1][k].isnumeric():
            k = j+1
        while j<=line_len and input_lines[index-1][k].isnumeric():
            number_str_2 += input_lines[index-1][k]
            k = k+1
    if j == line_len:
        k = j-1
        while k>=0 and input_lines[index][k].isnumeric():
            number_str_1 = input_lines[index][k] + number_str_1
            k -= 1
        k = j
        if not input_lines[index-1][k].isnumeric():
            k = j-1
        while k>=0 and input_lines[index-1][k].isnumeric():
            number_str_2 = input_lines[index-1][k] + number_str_2
            k -= 1
    return int(number_str_1) * int(number_str_2)
        
def edge_case_numbers(index, j, line_len, is_last_line=False):
    number_str_1 = ''
    number_str_2 = ''
            
    if j==line_len:
        k = j-1
        while input_lines[index][k].isnumeric():
            number_str_1 = input_lines[index][k] + number_str_1
            k -= 1
        k = j
        if not input_lines[index+1][k].isnumeric():
            k = j-1
        while input_lines[index+1][k].isnumeric():
            number_str_2 = input_lines[index+1][k] + number_str_2
            k -= 1
    else:
        k = j+1
        while input_lines[index][k].isnumeric():
            number_str_1 += input_lines[index][k]
            k = k +1
        k=j
        if not input_lines[index+1][k].isnumeric():
            k = j+1
        while input_lines[index+1][k].isnumeric():
            number_str_2 += input_lines[index+1][k]
            k = k+1
    return int(number_str_1) * int(number_str_2)

def get_numbers(index, j, line_len):
    number_str_1 = ''
    number_str_2 = ''
    if not input_lines[index+1][j].isnumeric():  # ....456/ 123.... / ....456
        if not input_lines[index+1][j+1].isnumeric():
            k = j-1
            while k >= 0 and input_lines[index+1][k].isnumeric():
                number_str_1 = input_lines[index+1][k] + number_str_1
                k -= 1
        else:
            k = j+1
            while k <= line_len and input_lines[index+1][k].isnumeric():
                number_str_1 += input_lines[index+1][k]
                k += 1
    else:
        k = j
        l = j-1
        while k <= line_len and input_lines[index+1][k].isnumeric():
            number_str_1 += input_lines[index+1][k]
            k += 1
        while l >= 0 and input_lines[index+1][l].isnumeric():
            number_str_1 = input_lines[index+1][l] + number_str_1
            l -= 1
    
    if not input_lines[index-1][j].isnumeric():  # ....456/ 123.... / ....456
        if not input_lines[index-1][j+1].isnumeric():
            k = j-1
            while k >= 0 and input_lines[index-1][k].isnumeric():
                number_str_2 = input_lines[index-1][k] + number_str_2
                k -= 1
        else:
            k = j+1
            while k <= line_len and input_lines[index-1][k].isnumeric():
                number_str_2 += input_lines[index-1][k]
                k += 1
    else:
        k = j
        l = j-1
        while k <= line_len and input_lines[index-1][k].isnumeric():
            number_str_2 += input_lines[index-1][k]
            k += 1
        while l >= 0 and input_lines[index-1][l].isnumeric():
            number_str_2 = input_lines[index-1][l] + number_str_2
            l -= 1
    return int(number_str_1) * int(number_str_2)

last_line = len(input_lines) - 1
total = 0
for index, line in enumerate(input_lines):
    last_char = len(line)-1
    for j, txt in enumerate(line):
        if txt == '*':
            if index == 0:
                if j == 0:
                    if (line[j+1].isnumeric()) and (input_lines[index+1][j].isnumeric() or input_lines[index+1][j+1].isnumeric()):
                        total+=edge_case_numbers(index, j, last_char)
                elif j == last_char:
                    if (line[j-1].isnumeric()) and (input_lines[index+1][j].isnumeric() or input_lines[index+1][j-1].isnumeric()):
                        total+=edge_case_numbers(index, j, last_char)
                else:
                    if (line[j-1].isnumeric() or line[j+1].isnumeric()) and (input_lines[index+1][j].isnumeric() or input_lines[index+1][j-1].isnumeric() or input_lines[index+1][j+1].isnumeric()):
                        total+=edge_case_numbers_two(index, j, last_char)
                    elif not input_lines[index+1][j].isnumeric() and input_lines[index+1][j+1].isnumeric() and input_lines[index+1][j-1].isnumeric():
                        total += new_flow(index+1, j, last_char)
                    elif line[j-1].isnumeric() and line[j+1].isnumeric():
                        total+=same_line_numaric(index, j, last_char)
            elif index  == last_line:
                if j ==0:
                    if line[j+1].isnumeric() and (input_lines[index-1][j].isnumeric() or input_lines[index-1][j+1].isnumeric()):
                        total+=edge_case_last_line(index, j, last_char)
                elif j == last_char:
                    if line[j-1].isnumeric() and (input_lines[index-1][j].isnumeric() or input_lines[index-1][j-1].isnumeric()):
                        total+=edge_case_last_line(index, j, last_char)
                else:
                    if not input_lines[index-1][j].isnumeric() and input_lines[index-1][j+1].isnumeric() and input_lines[index-1][j-1].isnumeric():
                        total += new_flow(index-1, j, last_char)
                    elif line[j-1].isnumeric() and line[j+1].isnumeric():
                        total+=same_line_numaric(index, j, last_char)
            else:
                if j == 0:
                    if (input_lines[index-1][j].isnumeric() or  input_lines[index-1][j+1].isnumeric()) and \
                        (input_lines[index+1][j].isnumeric() or input_lines[index+1][j+1].isnumeric()):
                        total+=get_numbers(index, j, last_char)
                elif j == last_char:
                    if (input_lines[index-1][j].isnumeric() or input_lines[index-1][j-1].isnumeric()) and \
                        (input_lines[index+1][j].isnumeric() or input_lines[index+1][j-1].isnumeric()):
                        total+=get_numbers(index, j, last_char)
                else:
                    if (line[j-1].isnumeric() or line[j+1].isnumeric()) and \
                        ((input_lines[index+1][j].isnumeric() or input_lines[index+1][j-1].isnumeric() or input_lines[index+1][j+1].isnumeric()) or \
                        (input_lines[index-1][j].isnumeric() or input_lines[index-1][j-1].isnumeric() or input_lines[index-1][j+1].isnumeric())):
                        total+=edge_case_numbers_two(index, j, last_char)
                    elif not input_lines[index-1][j].isnumeric() and input_lines[index-1][j+1].isnumeric() and input_lines[index-1][j-1].isnumeric():
                        total += new_flow(index-1, j, last_char)
                    elif not input_lines[index+1][j].isnumeric() and input_lines[index+1][j+1].isnumeric() and input_lines[index+1][j-1].isnumeric():
                        total += new_flow(index+1, j, last_char)
                    elif line[j-1].isnumeric() and line[j+1].isnumeric():
                        total+=same_line_numaric(index, j, last_char)
                    elif (input_lines[index-1][j].isnumeric() or  input_lines[index-1][j+1].isnumeric() or input_lines[index-1][j-1].isnumeric()) and \
                        (input_lines[index+1][j].isnumeric() or input_lines[index+1][j+1].isnumeric() or input_lines[index+1][j-1].isnumeric()):
                        total+=get_numbers(index, j, last_char)

print(total)
               
        # if gare:
        #     print(gare)
