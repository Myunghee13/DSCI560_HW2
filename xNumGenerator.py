# 1. a. Generate 1000 random numbers over the range 0-100
import random
import matplotlib.pyplot as plt
from pathlib import Path

random.seed(30)
output_folder = Path("output")

xNum = list()
with open(output_folder / "xNumbers.txt", "w") as f: 
    for i in range(1000):
        num = random.randint(0, 100)
        xNum.append(num)
        f.write(str(num)+'\n')

# drawing histogram of generated random numbers
import matplotlib.pyplot as plt

fig = plt.figure()
plt.hist(xNum,edgecolor='black')
plt.title("Histogram of 1000 random numbers")
plt.xlabel('random number values')
plt.ylabel('count')
plt.show()
fig.savefig(output_folder / 'histogramXvalues.png')