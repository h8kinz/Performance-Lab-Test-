import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
a = [i for i in range(1, n + 1)]
b = []
c = 0
while True:
    b.append(a[c])
    c = (c + (m - 1)) % n
    if c == 0:
        break
for i in range(len(b)):
    print(b[i], end='')