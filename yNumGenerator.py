# 1. b. Generate new numbers from the original 1000 using the equation y=3x+6
import re
import matplotlib.pyplot as plt
from pathlib import Path

output_folder = Path("output")

# read a_result
with open(output_folder / "xNumbers.txt",'r') as f:
    xNum = [int(ele.strip()) for ele in f.readlines()]

yNum = list()
with open(output_folder / "yNumbers.txt", "w") as f: 
    for num in xNum:
        ynum = 3*num+6
        yNum.append(ynum)
        f.write(str(ynum)+'\n')  # y = 3x+6        

# drawing histogram of generated y values
histogram = plt.hist(yNum,edgecolor='black')
plt.title("Histogram of y values")
plt.xlabel('y values')
plt.ylabel('count')
plt.show()

