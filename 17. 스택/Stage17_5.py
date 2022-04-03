import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    stack = list()
    stack_cal = list()
    is_it_able = True
    count = 1

    for _ in range(N):
        now_num = int(sys.stdin.readline().rstrip())
        while True:
            if len(stack) == 0:
                stack.append(count)
                stack_cal.append('+')
                count += 1

            elif stack[-1] == now_num:
                stack.pop()
                stack_cal.append('-')
                break

            elif stack[-1] > now_num:
                is_it_able = False
                break

            else:
                stack.append(count)
                stack_cal.append('+')
                count += 1

        if not is_it_able:
            break

    if is_it_able:
        for sp in stack_cal:
            print(sp)

    else:
        print('NO')
