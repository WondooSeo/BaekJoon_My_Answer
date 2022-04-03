import sys


def is_hansu(a):
	a_temp = a
	a_list = []
	while a_temp != 0:
		a_list.append(a_temp%10)
		a_temp = a_temp//10
	if a < 100:
		return True
	elif a >= 100 and a <= 999:
		if a_list[0] - a_list[1] == a_list[1] - a_list[2]:
			return True
		else:
			return False
	else:
		return False


if __name__ == '__main__':
	a = int(input())
	count = 0
	for i in range(a):
		if is_hansu(i+1):
			count += 1
	print(count)
