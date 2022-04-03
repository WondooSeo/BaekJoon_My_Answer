import sys

if __name__ == '__main__':
    a = int(input())
    b_list = list(map(int, sys.stdin.readline().rstrip().split()))
    b_list_sort = list(sorted(set(b_list)))
    dic_b = {b_list_sort[i]: i for i in range(len(b_list_sort))}
    for i in b_list:
        print(dic_b[i], end=' ')
