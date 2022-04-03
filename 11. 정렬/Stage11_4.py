import sys
from collections import Counter

if __name__ == '__main__':
	N = int(sys.stdin.readline().rstrip())
	num_list = list()

	for _ in range(N):
		num_list.append(int(sys.stdin.readline().rstrip()))

	if sum(num_list) >= 0:
		print(int(sum(num_list)/len(num_list) + 0.5))
	else:
		print(int(sum(num_list)/len(num_list) - 0.5))

	sorted_num_list = sorted(num_list)
	print(sorted_num_list[(N-1)//2])

	mode = Counter(sorted_num_list).most_common() 
	if len(mode) > 1:
		if mode[0][1] == mode[1][1]:
			print(mode[1][0])
		else:
			print(mode[0][0])

	else:
		print(mode[0][0])

	print(max(num_list)-min(num_list))
