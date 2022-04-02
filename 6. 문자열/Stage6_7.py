import sys

if __name__ == '__main__':
	a,b = map(str,sys.stdin.readline().rstrip().split())
	a = list(map(int,a))
	b = list(map(int,b))
	a.reverse()
	b.reverse()
	a = 100*a[0] + 10*a[1] + a[2]
	b = 100*b[0] + 10*b[1] + b[2]
	if a>=b:
		print(a)
	else:
		print(b)
