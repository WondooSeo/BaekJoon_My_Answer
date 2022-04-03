import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
	p1, p2 = map(int, sys.stdin.readline().rstrip().split())
	print(p1+p2)
