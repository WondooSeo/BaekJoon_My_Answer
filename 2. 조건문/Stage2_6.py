h, m = map(int,input().split())
c = int(input())

m = m+c%60
h = h+c//60

rm = m%60
ph = m//60
h = ph+h

if h>23:
	h=h%24

print(h,rm)
