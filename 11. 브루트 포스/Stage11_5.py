import sys

if __name__ == '__main__':
	n = int(sys.stdin.readline().rstrip())
	a = 666
	i = 1

	while i < n:
		a += 1
		if str(a).count('666')>0:
			i += 1

	print(a)
