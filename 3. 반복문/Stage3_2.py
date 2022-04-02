it = int(input())
a = list()

for i in range(it):
	t1, t2 = map(int,input().split())
	a.append((t1,t2))

for (t1,t2) in a:
	print(t1+t2)
