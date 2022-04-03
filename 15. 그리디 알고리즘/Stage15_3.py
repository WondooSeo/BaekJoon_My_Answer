import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    time_ATM = list(map(int, sys.stdin.readline().rstrip().split()))
    time_ATM.sort(reverse=True)
    time_count = 0

    for i in range(N):
        time_count += time_ATM[i]*(i+1)

    print(time_count)
