import sys


def prime_sleve(m, n):
    n_list = [1]*n
    sleve = []

    for i in range(1, n+1):
        if i == 1:
            n_list[i-1] = 0

        elif n_list[i-1] == 1:
            if i >= m and i <= n:
                print(i)
            temp = i*i
            while temp <= n:
                n_list[temp-1] = 0
                temp += i

        else:
            continue


if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().rstrip().split())
    prime_sleve(M, N)
