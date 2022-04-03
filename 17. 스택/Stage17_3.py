if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        PS = list(str(sys.stdin.readline().rstrip()))
        stack = []
        for ps_i in PS:
            if len(stack) > 0 and stack[-1] == '(' and ps_i == ')':
                stack.pop()
            else:
                stack.append(ps_i)

        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
