import sys
from collections import deque

if __name__ == '__main__':
    N,K = map(int,sys.stdin.readline().rstrip().split())
    N_queue = deque(list(range(N)))
    turn = 0
    josepus = []

    while len(N_queue) > 0:
        turn += 1
        if turn%K == 0:
            josepus.append(N_queue.popleft()+1)
        else:
            N_queue.append(N_queue.popleft())

    print('<',end='')
    for i in range(N):
        print(josepus[i],end='')
        if i == N-1:
            break
        else:
            print(', ',end='')
    print('>')
