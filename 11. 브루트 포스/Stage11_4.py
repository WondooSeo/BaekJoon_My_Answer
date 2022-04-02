import sys

if __name__ == '__main__':
    N,M = map(int,sys.stdin.readline().rstrip().split())
    chesspan = list()
    for _ in range(N):
        chesspan.append(list(sys.stdin.readline().rstrip()))

    count = list()

    for i in range(N-7):
        for j in range(M-7):
            count1 = 0; count2 = 0;
            for k in range(i,i+8):
                for l in range(j,j+8):
                    if (k+l)%2 == 0:
                        if chesspan[k][l] == 'W':
                            count1 += 1
                        if chesspan[k][l] == 'B':
                            count2 += 1

                    else:
                        if chesspan[k][l] == 'B':
                            count1 += 1
                        if chesspan[k][l] == 'W':
                            count2 += 1

            count.append(min(count1,count2))

    print(min(count))
