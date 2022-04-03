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
    my_sleve = prime_sleve(1000)
    N = int(sys.stdin.readline().rstrip())
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))
    count = 0

    for num in num_list:
        if my_sleve.count(num) > 0:
            count += 1

    print(count)
