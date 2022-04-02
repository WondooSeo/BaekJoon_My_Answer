import sys

def int_tri(N):
    input_tri = list()
    for i in range(N):
        input_tri.append(list(map(int,sys.stdin.readline().rstrip().split())))

    for i in reversed(range(N-1)):
        for j in range(len(input_tri[i])):
            input_tri[i][j] += max(input_tri[i+1][j],input_tri[i+1][j+1])

    print(input_tri[0][0])


if __name__ == '__main__':
    int_tri(int(sys.stdin.readline().rstrip()))
