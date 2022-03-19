import sys
from collections import deque

if __name__ == '__main__':
    
    N,M = map(int,sys.stdin.readline().rstrip().split())
    N_list = deque(list(range(1,N+1)))
    pop_list = list(map(int,sys.stdin.readline().rstrip().split()))
    count = 0

    for i in range(M):
        while True:
            if N_list[0] == pop_list[i]:
                N_list.popleft()
                break
            elif N_list.index(pop_list[i]) <= len(N_list)//2:
                N_list.append(N_list.popleft())
                count += 1
            else:
                N_list.appendleft(N_list.pop())
                count += 1


    print(count)
