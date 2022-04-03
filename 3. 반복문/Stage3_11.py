import sys

if __name__ == '__main__':
	n, x = map(int, sys.stdin.readline().rstrip().split())
	a = list(map(int, sys.stdin.readline().rstrip().split()))

	for i in range(n):
		if a[i] < x:
			print(a[i], end=' ')
