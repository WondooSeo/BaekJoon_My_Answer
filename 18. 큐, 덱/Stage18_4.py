import sys
from collections import deque

if __name__ == '__main__':
	N = int(sys.stdin.readline().rstrip())

	for _ in range(N):
		N, M = map(int, sys.stdin.readline().rstrip().split())
		print_queue = deque([])

		print_importance = list(map(int, sys.stdin.readline().rstrip().split()))
		for i in range(len(print_importance)):
			print_queue.append(print_importance[i])
			if i == M:
				print_queue.append(0)

		print_num = 0

		while True:
			if print_queue[0] != max(print_queue):
				print_queue.append(print_queue.popleft())
				if print_queue[0] == 0:
					print_queue.append(print_queue.popleft())

			else:
				print_queue.popleft()
				print_num += 1
				if print_queue[0] == 0:
					break

		print(print_num)
