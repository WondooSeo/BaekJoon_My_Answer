import sys

if __name__ == '__main__':
	a = int(input())
	ans = list()
	for i in range(a):
		result = list(input())
		score = 0
		streak = 0
		for j in range(len(result)):
			if result[j] == 'O':
				streak += 1
			else:
				streak = 0
			score += streak
		print(score)
