import sys
task4 = sys.argv[1]
with open (task4,'r') as inf:
    a = inf.readlines()
for i in range(len(a)):
    a[i] = int(a[i])
a = sorted(a)
m = len(a)//2
b = a[m]
c = 0
for i in range(len(a)):
    d = abs(a[i] - b)
    c += d
print(c)

