import sys

if __name__ == '__main__':
	a_list = list()
	for i in range(10):
		a_list.append(int(input()))
	judge = [0]*42
	len_a_list = len(a_list)
	for i in range(len_a_list):
		judge[a_list[i]%42] = 1
	ans = 0
	for i in range(42):
		ans += judge[i]
	print(ans)
