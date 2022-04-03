'''
# Time Over version

import sys

def nge(n, n_list):
    max_nge = -1
    while len(n_list) > n+1:
        temp = n_list.pop()
        if temp > n_list[n]:
            max_nge = temp

    return max_nge

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(N):
        temp_list = num_list.copy()
        print(nge(i,temp_list),end=' ')
'''

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))

    nge = [-1]*N
    num_stack = list()

    for i in range(N):
        while len(num_stack) != 0 and num_list[num_stack[-1]] < num_list[i]:
            nge[num_stack[-1]] = num_list[i]
            num_stack.pop()

        num_stack.append(i)

    print(*nge)
