if __name__ == '__main__':
	a = int(input())
	b = int(input())
	ttl = 0
	for i in range(a):
		ttl += b%10
		b = b//10

	print(ttl)
