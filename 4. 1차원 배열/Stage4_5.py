import sys

if __name__ == '__main__':
	a = int(input())
	a_list = list(map(int, sys.stdin.readline().rstrip().split()))
	score = sum(a_list)
	print(score/max(a_list)/len(a_list)*100)
