import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().rstrip().split())
    money_unit_list = list()

    for _ in range(N):
        money_unit_list.append(int(sys.stdin.readline().rstrip())) 

    count = 0

    for money_unit in money_unit_list[::-1]:
        if K >= money_unit:
            count += K//money_unit
            K -= money_unit*(K//money_unit)

        elif K == 0:
            break

        else:
            continue

    print(count)
