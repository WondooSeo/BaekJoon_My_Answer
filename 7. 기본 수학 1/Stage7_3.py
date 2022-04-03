if __name__ == '__main__':
    X = int(input())
    n = 1
    count = 0
    while True:
        count += n
        if count >= X:
            break
        n += 1
    loc = count - X
    if n%2 == 0:
        bunja = n-loc
        bunmo = loc+1
        print(str(bunja)+'/'+str(bunmo))
    else:
        bunja = loc+1
        bunmo = n-loc
        print(str(bunja)+'/'+str(bunmo))
