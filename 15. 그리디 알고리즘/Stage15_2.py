import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    conf_time = list()

    for _ in range(n):
        conf_time.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # We have to sort with start time after sorting finish time
    # Ex) If there are [6, 6] and [5, 6], we have to choose both of them, not only [6, 6]
    conf_time.sort(key=lambda x: (x[1], x[0]))
    total_conf = list()
    finish_time = conf_time[0][1]
    count = 1

    for i in range(1, n):
        if conf_time[i][0] >= finish_time:
            finish_time = conf_time[i][1]
            count += 1

    print(count)
