import sys

if __name__ == '__main__':
	N = int(sys.stdin.readline().rstrip())
	count = N

	for _ in range(N):
		input_str = sys.stdin.readline().rstrip()
		
		for i in range(len(input_str)-1):
			if input_str[i] == input_str[i+1]:
				continue
			elif input_str[i] in input_str[i+1:]:
				count -= 1
				break

	print(count)