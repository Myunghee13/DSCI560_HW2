# 1. b. Generate new numbers from the original 1000 using the equation y=3x+6
import re

# read a_result
result1 = list()
with open("xNumbers.txt", "r") as f: 
    lines = f.readlines()
    for num in lines:
        result1.append(int(re.sub(r"\n", "", num)))

with open("yNumbers.txt", "w") as f: 
    for num in result1:
        f.write(str(3*num+6)+'\n')  # y = 3x+6        



