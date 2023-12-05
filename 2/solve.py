import fileinput
import re

pattern = re.compile(r'(\d+) green, (\d+) red, (\d+) blue')

c = 1
def solve_line(line):
    matches = pattern.findall(line)
    for match in matches:
        ig,ir,ib = map(int,match)
        if ir > 12 or ig > 13 or ib > 14: return False

    return True

sum = 0
i = 1
for line in fileinput.input():
    sum += i if solve_line(line) else 0
    i+=1

print(sum)