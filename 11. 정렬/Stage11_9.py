import sys
from collections import Counter

if __name__ == '__main__':
	N = int(sys.stdin.readline().rstrip())
	signin_list = []

	for _ in range(N):
		signin_list.append(list(sys.stdin.readline().rstrip().split()))

	signin_list = sorted(signin_list, key=lambda x: (int(x[0])))
	for signin in signin_list:
		print(signin[0], signin[1])
