import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
	p1,p2 = map(int,sys.stdin.readline().rstrip().split())
	print('Case #'+str(i+1)+': '+str(p1)+' + '+str(p2)+' = '+str(p1+p2))
