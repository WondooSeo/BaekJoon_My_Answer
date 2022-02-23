import sys

if __name__ == '__main__':
	while True:
		a,b = map(int,sys.stdin.readline().rstrip().split())
		
		if a==0 and b==0:
			break
		else:
			print(a+b)
