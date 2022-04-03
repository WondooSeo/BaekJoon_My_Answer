import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    list_A = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    M = int(sys.stdin.readline().rstrip())
    searching_list = list(map(int, sys.stdin.readline().rstrip().split()))

    for searching_num in searching_list:
        start = 0; end = N-1;
        while end > start:
            middle = (start+end)//2
            if list_A[middle] > searching_num:
                end = middle - 1
            elif list_A[middle] < searching_num:
                start = middle + 1
            else:
                start = middle
                break

        if list_A[start] == searching_num:
            print(1)
        else:
            print(0)
