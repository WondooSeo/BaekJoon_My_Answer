import sys

if __name__ == '__main__':
	a = list(input())
	loc_alp = [-1]*26
	for i in range(len(a)):
		alp = ord(a[i]) - ord('a')
		if loc_alp[alp] == -1:
			loc_alp[alp] = i
	for i in loc_alp:
		print(i,end=' ')
