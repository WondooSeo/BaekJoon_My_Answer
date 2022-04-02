import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())

    dungchi = list()
    for _ in range(n):
        dungchi.append(list(map(int,sys.stdin.readline().rstrip().split())))

    dungchi_rank = list()
    for i in range(len(dungchi)):
        smaller_than_me = 0;
        for j in range(len(dungchi)):
            if i == j:
                continue

            elif dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
                smaller_than_me += 1

        dungchi_rank.append(smaller_than_me)

    for now_smaller_than_me in dungchi_rank:
        print(now_smaller_than_me+1,end=' ')
