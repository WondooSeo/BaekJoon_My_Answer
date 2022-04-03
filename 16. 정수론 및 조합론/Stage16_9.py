import sys


def factorial(a):
	if a > 0:
		return a*factorial(a-1)
	else:
		return 1


if __name__ == '__main__':
	tc = int(sys.stdin.readline().rstrip())

	for i in range(tc):
		n, m = map(int, sys.stdin.readline().rstrip().split())
		comb = int(factorial(max(n, m))/(factorial(min(n, m))*factorial(abs(n-m))))
		print(comb)
