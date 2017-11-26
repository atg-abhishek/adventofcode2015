from pprint import pprint 
inp = ""
with open('../Data/day1.txt') as infile:
    inp = infile.read()

floor = 0
res_index = 1
for ind, x in enumerate(list(inp)):
    if x=='(':
        floor+=1
    else:
        floor-=1
    if floor==-1:
        res_index = ind+1
        break 
pprint(res_index)
pprint(floor)