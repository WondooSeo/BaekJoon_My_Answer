import sys

if __name__ == '__main__':
	a = int(input())
	b = int(input())
	c = int(input())
	r = list(map(int, str(a*b*c)))
	ans = [0]*10
	for i in range(len(r)):
		ans[r[i]] += 1
	for i in range(len(ans)):
		print(ans[i])
