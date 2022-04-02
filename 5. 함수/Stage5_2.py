import sys

def d(a):
	a_temp = a
	a_list = []
	while a_temp != 0:
		 a_list.append(int(a_temp%10))
		 a_temp = a_temp//10
	da = a + sum(a_list)
	return da

if __name__ == '__main__':
	a = [1]*10000
	for i in range(0,10000):
		b = i + 1
		dn = d(b)
		if dn <= 10000:
			a[dn-1] = 0
			
	for i in range(0,10000):
		if a[i] == 1:
			print(i+1)
