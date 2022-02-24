import sys

if __name__ == '__main__':
	a = int(input())
	for i in range(a):
		testcase = list(map(int,sys.stdin.readline().rstrip().split()))
		testcase_avg = (sum(testcase)-testcase[0])/testcase[0]
		up_avg = 0
		for j in range(testcase[0]):
			if testcase[j+1]>testcase_avg:
				up_avg+=1
		not_avg_p = up_avg/testcase[0]*100
		print('%.3f' % not_avg_p + '%')
