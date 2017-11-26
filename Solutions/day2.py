from pprint import pprint 
li = []
with open("../Data/day2.txt") as infile:
    li = infile.readlines()

total_sheet = 0
ribbon = 0
for dimensions in li:
    l,w,h = map(int, dimensions.split('x'))
    slack_size = min(l*w, w*h, h*l)
    total_sheet += 2*(l*w + w*h + h*l) + slack_size
    smallest_side = min(l+w, w+h, h+l)
    ribbon += smallest_side*2 + l*w*h

pprint(ribbon)
pprint(total_sheet)