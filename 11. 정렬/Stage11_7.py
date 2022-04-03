import sys

if __name__ == '__main__':
	N = int(sys.stdin.readline().rstrip())
	point_list = []

	for _ in range(N):
		point = list(map(int, sys.stdin.readline().rstrip().split()))
		point_list.append(point[::-1])

	sorted_y = sorted(point_list)
	
	for i in range(N):
		print(sorted_y[i][1], sorted_y[i][0])
