import sy

def fibo_dp(num):
    f0 = [1, 0, 1]
    f1 = [0, 1, 1]

    if num >= 3:
        for i in range(3, num+1):
            # fib(n) = fib(n-1) + fib(n-2)
            f0.append(f0[i-1] + f0[i-2])
            f1.append(f1[i-1] + f1[i-2])

    print(f0[num], f1[num])


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        fibo_dp(int(sys.stdin.readline().rstrip()))
