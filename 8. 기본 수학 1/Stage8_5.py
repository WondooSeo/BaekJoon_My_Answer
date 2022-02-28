import sys

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        H,W,N = map(int,sys.stdin.readline().rstrip().split())
        room = 100*((N-1)%H+1)+(N-1)//H+1
        print(room)
