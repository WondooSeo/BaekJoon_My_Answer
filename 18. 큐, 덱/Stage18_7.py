import sys
from collections import deque

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    
    for _ in range(N):
        cmd_deque = deque(list(sys.stdin.readline().rstrip()))
        array_num = int(sys.stdin.readline().rstrip())
        array = list(str(sys.stdin.readline().rstrip()))
        array = ''.join(array[1:-1])

        if len(array) != 0:
            array = deque(list(array.split(',')))
        else:
            array = deque(list())

        if cmd_deque.count('D') > len(array):
            print('error')
        else:
            count_R = 0
            for cmd in cmd_deque:
                if cmd == 'R':
                    count_R += 1
                else:
                    if count_R%2 == 0:
                        array.popleft()
                    else:
                        array.pop()

            if count_R%2 == 0:
                print('['+','.join(list(array))+']')
            else:                
                print('['+','.join(reversed(array))+']')
