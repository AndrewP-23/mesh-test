import matplotlib.pyplot as plt
import numpy as np
import re


def process(cmd, points):
    res = points
    if cmd == "count":
        print(points.shape[0])
    if cmd == "print":
        print(points)
    if cmd.startswith("rm"):
        z_range = list(map(float, re.findall(r"[-+]?\d*\.?\d+", cmd)))
        res = points[((points[:, 2] > z_range[1]) | (points[:, 2] < z_range[0]))]
    if cmd == "hist":
        n, bins, patches = plt.hist(points[:, 2], bins='auto', rwidth=1)
        plt.grid(axis='y')
        plt.xlabel('Z')
        plt.ylabel('Count')
        maxc = n.max()
        plt.ylim(ymax=np.ceil(maxc / 10) * 10 if maxc % 10 else maxc + 10)
        plt.show()
    return res


if __name__ == '__main__':
    filename = input()
    points = np.empty((0, 3))
    with open(filename) as f:
        for line in f.readlines():
            points = np.append(points, np.array([[float(x) for x in line.split()]]), axis=0)
    while True:
        cmd = input()
        if cmd == "exit":
            break
        points = process(cmd, points)
