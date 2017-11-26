from pprint import pprint 

inp = ""
with open("../Data/day3.txt") as infile:
    inp = infile.read()

def part1(instructions=inp):
    x,y = 0,0
    houses_visited = set()
    houses_visited.add((x,y))
    counter = 1
    for instruction in instructions:
        if instruction == "^":
            y+=1
        if instruction == "v":
            y-=1
        if instruction == ">":
            x+=1
        if instruction == "<":
            x-=1
        if (x,y) not in houses_visited:
            houses_visited.add((x,y))
            counter+=1

    return houses_visited

def part2():
    santa_instructions_list = inp[0::2]
    robo_instructions_list = inp[1::2]
    santa_houses = part1(santa_instructions_list)
    robo_houses = part1(robo_instructions_list)

    return len(santa_houses.union(robo_houses))

pprint(part2())