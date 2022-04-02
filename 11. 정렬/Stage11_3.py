import sys

if __name__ == '__main__':

    # Counting sort
    N = int(sys.stdin.readline().rstrip())
    num_list = [0]*10000

    for _ in range(N):
        now_num = int(sys.stdin.readline().rstrip())
        num_list[now_num-1] += 1

    for i in range(len(num_list)):
        while num_list[i] > 0:
            print(i+1)
            num_list[i] -= 1
