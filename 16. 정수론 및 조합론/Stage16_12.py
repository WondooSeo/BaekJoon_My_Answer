import sys

def count_two(temp):
    num_two = 0
    while temp != 0:
        temp = temp//2
        num_two += temp

    return num_two


def count_five(temp):
    num_five = 0
    while temp != 0:
        temp = temp//5
        num_five += temp

    return num_five


if __name__ == '__main__':

    N, M = map(int,sys.stdin.readline().rstrip().split())

    print(min(count_two(N)-count_two(N-M)-count_two(M),count_five(N)-count_five(N-M)-count_five(M)))
