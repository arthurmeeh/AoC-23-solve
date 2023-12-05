import fileinput
import re
from typing import Iterator

sum=0


# Day 1.
# for line in fileinput.input():
#     num = 0
#     for c in line:
#         if c >= '0' and c <= '9':
#             num = int(c)
#             break
#     for c in line[::-1]:
#         if c >= '0' and c <= '9':
#             num = (10 * num + int(c))
#             break
#     sum += num

# Day 2.
wm={"one":'o1e',"two":'t2o',"three":'t3e',"four":'4',"five":'5e',"six":'6',"seven":'7n',"eight":'e8t',"nine":'n9e'}

def solve_line(word):
    ret = 0
    for w,n in wm.items():
        word = word.replace(w,n)
    for i in word: 
        if (i>='0' and i<='9'):
            ret = int(i)
            break
    for i in reversed(word):
        if (i>='0' and i<='9'):
            ret = 10*ret+int(i)
            break
    return ret 
        
for line in fileinput.input():
    num = solve_line(line)
    sum += num 
    print(f'{line[0:len(line)-1]}--{num}')

print(f"SOLVE:{sum}")