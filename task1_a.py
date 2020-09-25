# 1. a. Generate 1000 random numbers over the range 0-100
import random

random.seed(30)

with open("a_result.txt", "w") as f: 
    for i in range(1000):
        num = random.randint(0, 100)
        f.write(str(num)+'\n')