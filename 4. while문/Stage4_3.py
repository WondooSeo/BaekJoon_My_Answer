if __name__ == '__main__':
	a = int(input())
	at = a
	t = 0;
	while True:
		a1 = at//10
		a2 = at%10
		b = (a1+a2)%10
		c = a2*10 + b
		t += 1
		if a == c:
			break
		at = c
	print(t)
