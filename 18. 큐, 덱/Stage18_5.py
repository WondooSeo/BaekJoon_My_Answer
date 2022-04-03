import sys
from collections import deque

if __name__ == '__main__':
    N = int(input())
    queue = deque(list())

    for _ in range(N):
        com = sys.stdin.readline().rstrip().split()
        if com[0] == 'push_front':
            queue.appendleft(int(com[1]))

        elif com[0] == 'push_back':
            queue.append(int(com[1]))

        elif com[0] == 'pop_front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())

        elif com[0] == 'pop_back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.pop())

        elif com[0] == 'size':
            print(len(queue))

        elif com[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)

        elif com[0] == 'front':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])

        elif com[0] == 'back':
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])
