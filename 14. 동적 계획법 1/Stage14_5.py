import sys

def RGB_cost(n):
    cost_list = list()
    for _ in range(n):
        cost_list.append(list(map(int,sys.stdin.readline().rstrip().split())))

    for i in range(1,n):
        cost_list[i][0] = min(cost_list[i-1][1],cost_list[i-1][2]) + cost_list[i][0]
        cost_list[i][1] = min(cost_list[i-1][0],cost_list[i-1][2]) + cost_list[i][1]
        cost_list[i][2] = min(cost_list[i-1][0],cost_list[i-1][1]) + cost_list[i][2]

    print(min(cost_list[n-1]))

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    RGB_cost(N)
