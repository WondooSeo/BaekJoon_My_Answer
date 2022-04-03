import sys


def bin_tile(n):
    total_tile = [1, 2]
    if n > len(total_tile):
        for i in range(len(total_tile), n+1):
            # mod 15476 here to avoid memory limit exceed
            total_tile.append((total_tile[i-1]+total_tile[i-2])%15746)

    return total_tile[n-1]


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    print(bin_tile(N))
