import sys


def prime_sleve(n):
    n_list = [1]*n
    sleve = []

    for i in range(1, n+1):
        if i == 1:
            n_list[i-1] = 0

        elif n_list[i-1] == 1:
            sleve.append(i)
            temp = i*i
            while temp <= n:
                n_list[temp-1] = 0
                temp += i

        else:
            continue

    return sleve


if __name__ == '__main__':
    my_sleve = prime_sleve(10000)
    M = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    count = []
    for i in range(M, N+1):
        if my_sleve.count(i) > 0:
            count.append(i)

    if len(count) > 0:
        print(sum(count))
        print(count[0])
    else:
        print(-1)
