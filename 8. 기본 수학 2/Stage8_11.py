import sys

if __name__ == '__main__':
	a = int(input())
	for i in range(a):
		x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
		turret_dist = ((x1-x2)**2+(y1-y2)**2)**0.5
		r_min = min(r1, r2)
		r_max = max(r1, r2)
		r_sum = r_max + r_min
		r_diff = r_max - r_min

		if x1 == x2 and y1 == y2 and r1 == r2:
			print(-1)

		elif turret_dist > r_sum:
			print(0)

		elif turret_dist == r_sum:
			print(1)

		elif turret_dist < r_sum and turret_dist > r_diff:
			print(2)

		elif turret_dist == r_diff:
			print(1)

		elif turret_dist < r_diff:
			print(0)
