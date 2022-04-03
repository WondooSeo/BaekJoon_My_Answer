if __name__ == '__main__':
    n = int(input())
    M = 0

    for i in range(1, n):
        i_list = list(map(int, str(i)))
        if i + sum(i_list) == n:
            M = i
            break

    print(M)
