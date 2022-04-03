import sys

def prime_sleve(a):
	is_prime = [1]*a
	sleve = []

	for i in range(1, int(a**(0.5))+1):
		if i == 1:
			is_prime[i-1] = 0

		elif is_prime[i-1] == 1:
			temp = i+i
			while temp <= a:
				is_prime[temp-1] = 0
				temp += i

		else:
			continue

	for j in range(len(is_prime)):
		if is_prime[j] == 1:
			sleve.append(j+1)

	return sleve


if __name__ == '__main__':
	my_sleve = prime_sleve(10000)
	n = int(sys.stdin.readline().rstrip())

	for _ in range(n):
		now_even = int(sys.stdin.readline().rstrip())
		p = now_even // 2; q = now_even // 2;
		while True:
			if p in my_sleve and q in my_sleve:
				break

			else:
				p -= 1; q += 1;

		print(p,q)
