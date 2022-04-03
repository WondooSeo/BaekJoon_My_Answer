import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    card = list(map(int, sys.stdin.readline().rstrip().split()))
    
    global_max = -1

    for i in range(N-2):
        for j in range(i+1, N-1, 1):
            for k in range(j+1, N, 1):
                card_sum = card[i]+card[j]+card[k]
                if card_sum <= M and card_sum > global_max:
                    global_max = card_sum

    print(global_max)
