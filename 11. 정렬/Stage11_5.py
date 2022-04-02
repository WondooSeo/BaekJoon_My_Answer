import sys

if __name__ == '__main__':
	a = list(map(int,sys.stdin.readline().rstrip()))
	a = sorted(a,reverse=True)

	for num in a:
		print(num,end='')
