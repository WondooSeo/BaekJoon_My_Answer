a, b, c = map(int, input().split())

if a == b and b == c and c == a:
	p = 10000+a*1000
elif a == b and b != c and a != c:
	p = 1000+a*100
elif a != b and b == c and a != c:
	p = 1000+b*100
elif a != b and b != c and a == c:
	p = 1000+c*100
else:
	p = max(a, b, c)*100

print(p)
