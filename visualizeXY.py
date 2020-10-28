# 1. c. Visualize the results

import re
# read a_result, b_result
a_result = list()
with open("xNumbers.txt", "r") as f: 
    lines = f.readlines()
    for num in lines:
        a_result.append(int(re.sub(r"\n", "", num)))
b_result = list()
with open("yNumbers.txt", "r") as f: 
    lines = f.readlines()
    for num in lines:
        b_result.append(int(re.sub(r"\n", "", num)))

# visualize graph
import matplotlib.pyplot as plt

fig = plt.figure()
plt.scatter(a_result, b_result)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

fig.savefig('xyGraph.png')
