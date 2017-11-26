from pprint import pprint 
from collections import defaultdict
li = []
with open('../Data/day6.txt') as infile:
    li = infile.readlines()

def part1():
    lights_matrix = defaultdict(bool)
    for instruction in li:
        words = instruction.split(" ")
        if words[0] == "turn":
            start = words[2]
            start_x = int(start.split(',')[0])
            start_y = int(start.split(',')[1])
            end = words[-1]
            end_x = int(end.split(',')[0])
            end_y = int(end.split(',')[1])
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y+1):
                    if words[1] == 'on':
                        lights_matrix[(x,y)] = True
                    if words[1] == "off":
                        lights_matrix[(x,y)] = False
        if words[0] == "toggle":
            start = words[1]
            start_x = int(start.split(',')[0])
            start_y = int(start.split(',')[1])
            end = words[-1]
            end_x = int(end.split(',')[0])
            end_y = int(end.split(',')[1])
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y+1):
                    if (x,y) in lights_matrix:
                        lights_matrix[(x,y)] = not lights_matrix[(x,y)]
                    else:
                        lights_matrix[(x,y)] = True
    count = 0
    for k,v in lights_matrix.items():
        if v:
            count+=1

    pprint(count)

def part2():
    lights_matrix = defaultdict(int)

    def manage_lights(coords, instruction):
        if instruction == "on":
            if coords in lights_matrix:
                lights_matrix[coords] += 1
            else:
                lights_matrix[coords] = 1
        if instruction == "off":
            if coords in lights_matrix:
                if lights_matrix[coords] >= 1:
                    lights_matrix[coords] -= 1
                else:
                    lights_matrix[coords] = 0
        if instruction == "toggle":
            if coords in lights_matrix:
                lights_matrix[coords] += 2
            else:
                lights_matrix[coords] = 2

    for instruction in li:
        words = instruction.split(" ")
        if words[0] == "turn":
            start = words[2]
            start_x = int(start.split(',')[0])
            start_y = int(start.split(',')[1])
            end = words[-1]
            end_x = int(end.split(',')[0])
            end_y = int(end.split(',')[1])
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y+1):
                    if words[1] == 'on':
                        manage_lights((x,y), "on")
                    if words[1] == "off":
                        manage_lights((x,y), "off")
        if words[0] == "toggle":
            start = words[1]
            start_x = int(start.split(',')[0])
            start_y = int(start.split(',')[1])
            end = words[-1]
            end_x = int(end.split(',')[0])
            end_y = int(end.split(',')[1])
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y+1):
                    manage_lights((x,y), "toggle")
    
    
    
    brightness = 0
    for k,v in lights_matrix.items():
        brightness+=v

    pprint(brightness)

part2()