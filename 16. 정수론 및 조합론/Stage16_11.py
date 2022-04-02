import sys

if __name__ == '__main__':

    N = int(sys.stdin.readline().rstrip())
    count_2 = 0; count_5 = 0;

    for num in range(1,N+1):
        if num%5 == 0:
            while num%5 == 0:
                count_5 += 1
                num = num//5

        if num%2 == 0:
            while num%2 == 0:
                count_2 += 1
                num = num//2

    print(min(count_2,count_5))
