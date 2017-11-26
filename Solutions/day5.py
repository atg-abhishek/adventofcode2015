from pprint import pprint
li = []
with open('../Data/day5.txt') as infile:
    li = infile.readlines()

def part1():  
    nice_strings = 0
    for line in li:
        vowel_count = 0
        double_present = False
        for char in line:
            if char in ['a','e', 'i', 'o', 'u']:
                vowel_count+=1
        temp_line = line[1:]
        for ind, char in enumerate(temp_line):
            if char==line[ind]: #because the ind value starts one ahead, to look at the previous character in the original string we don't have to do -1
                
                double_present = True
                break
        if vowel_count>=3 and double_present:
            forbidden_strings = ['ab', 'cd', 'pq','xy']
            forbidden_present = False
            for fs in forbidden_strings:
                if fs in line:
                    forbidden_present = True
                    break
            if not forbidden_present:
                nice_strings += 1

def part2():
    nice_strings = 0
    for line in li:
        duplicate_present = False
        single_repeat = False
        for idx, char in enumerate(line[:-2]):
            if line[idx]+line[idx+1] in line[idx+2:]:
                duplicate_present = True
                break
        for idx, char in enumerate(line[:-2]):
            if char==line[idx+2] and char!=line[idx+1]:
                single_repeat = True
                break 
        if single_repeat and duplicate_present:
            nice_strings+=1
    pprint(nice_strings)
part2()