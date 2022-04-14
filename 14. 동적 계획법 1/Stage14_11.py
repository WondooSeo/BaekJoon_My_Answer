import sys

# LIS (Longest Increaing Subsequence)

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    now_list = list(map(int, sys.stdin.readline().rstrip().split()))
    increment_list = [1] * n

    for i in range(n):
        for j in range(i):
            if now_list[j] < now_list[i]:
                increment_list[i] = max(increment_list[i], increment_list[j]+1)

    print(max(increment_list))
