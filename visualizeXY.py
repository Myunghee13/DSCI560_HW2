# 1. c. Visualize the results

from pathlib import Path
import matplotlib.pyplot as plt

output_folder = Path("output")

# read intermediate results
with open(output_folder / "xNumbers.txt",'r') as f:
    xNum = [int(ele.strip()) for ele in f.readlines()]

with open(output_folder / "yNumbers.txt",'r') as f:
    yNum = [int(ele.strip()) for ele in f.readlines()]

# visualize graph

fig = plt.figure()
plt.scatter(xNum, yNum)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

fig.savefig(output_folder / 'xyGraph.png')
