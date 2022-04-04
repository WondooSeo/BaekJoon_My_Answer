import sys

if __name__ == '__main__':
    city_num = int(sys.stdin.readline().rstrip())
    road_dist = list(map(int, sys.stdin.readline().rstrip().split()))
    gas_cost = list(map(int, sys.stdin.readline().rstrip().split()))

    now_gas_cost = gas_cost[0]
    now_dist = road_dist[0]
    total_cost = 0

    for i in range(1, city_num-1):
        if now_gas_cost > gas_cost[i]:
            total_cost += now_gas_cost*now_dist
            now_gas_cost = gas_cost[i]
            now_dist = road_dist[i]

        else:
            now_dist += road_dist[i]

    total_cost += now_gas_cost * now_dist

    print(total_cost)
