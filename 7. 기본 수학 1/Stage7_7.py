import sys

if __name__ == '__main__':
	a = int(input())
	count = 0
	while a >= 0:
		if a%5 == 0:
			count += a//5
			a -= 5*a//5
			break
		a -= 3
		count += 1

	if a == 0:
		print(count)
	else:
		print(-1)
