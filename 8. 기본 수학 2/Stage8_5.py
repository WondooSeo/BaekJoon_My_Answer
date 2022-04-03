import sys


def prime_sleve(a, b):
	is_prime = [1]*b
	sleve = []

	for i in range(1, int(b**(0.5))+1):
		if i == 1:
			is_prime[i-1] = 0

		elif is_prime[i-1] == 1:
			temp = i+i
			while temp <= b:
				is_prime[temp-1] = 0
				temp += i

		else:
			continue

	for j in range(a+1, b+1):
		if is_prime[j-1] == 1:
			sleve.append(j)

	return sleve


if __name__ == '__main__':
	while True:
		n = int(sys.stdin.readline().rstrip())
		if n == 0:
			break

		now_sleve = prime_sleve(n, 2*n)
		print(len(now_sleve))
