import sys

if __name__ == '__main__':
	a = int(input())
	a_list = list(map(int, sys.stdin.readline().rstrip().split()))
	print(min(a_list), max(a_list))
