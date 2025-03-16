import math
import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
with open(file1, 'r') as inf:
    cx, cy = map(float, inf.readline().split())
    r = float(inf.readline())
a = []
with open (file2, 'r') as inf:
    for line in inf:
        px, py = map(float, line.split())
        a.append((px, py))
for x, y in a:
    d = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    if d == r:
        print(0)
    elif d < r:
        print(1)
    elif d > r:
        print(2)
    

