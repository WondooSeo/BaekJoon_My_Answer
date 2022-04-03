import sys
from collections import deque

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    card_deque = deque(list(range(1, N+1)))

    while len(card_deque) > 1:
        card_deque.popleft()
        card_deque.append(card_deque.popleft())

    print(card_deque[0])
