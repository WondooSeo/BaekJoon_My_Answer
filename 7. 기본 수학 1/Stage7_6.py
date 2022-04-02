import sys

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        zero_floor = list(range(1,n+1))
        total_floor = []
        total_floor.append(zero_floor)
        for i in range(k):
            now_floor = [1]
            for j in range(n-1):
                now_floor.append(total_floor[-1][j+1]+now_floor[-1])
            
            total_floor.append(now_floor)
        print(total_floor[-1][n-1])
