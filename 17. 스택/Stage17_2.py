import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    stack = []

    for _ in range(N):
        num = int(sys.stdin.readline().rstrip())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    print(sum(stack))
