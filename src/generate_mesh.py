import random


filename = "mesh.txt"
range_min = -30
range_max = 30
count = 1000

with open(filename, 'w') as f:
    for _ in range(count):
        for _ in range(3):
            f.write(str(random.uniform(range_min, range_max)) + " ")
        f.write("\n")
