if __name__ == '__main__':
    X = int(input())
    n = 1
    count = 1
    while True:
        if count >= X:
            break
        count += 6*n
        n += 1
    print(n)
