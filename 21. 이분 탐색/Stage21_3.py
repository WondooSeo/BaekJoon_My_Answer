import sys

if __name__ == '__main__':
    K, N = list(map(int, sys.stdin.readline().rstrip().split()))
    lan_list = list()
    for _ in range(K):
        lan_list.append(int(sys.stdin.readline().rstrip()))

    start = 1; end = max(lan_list)

    while start <= end:
        middle = (start+end)//2
        lan_num = 0
        for lan in lan_list:
            lan_num += lan//middle

        if lan_num < N:
            end = middle - 1

        else:
            start = middle + 1

    print(end)
