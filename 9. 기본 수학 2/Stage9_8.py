import sys

if __name__ == '__main__':
    x = []; y = [];
    for _ in range(3):
        xt,yt = map(int,sys.stdin.readline().rstrip().split())
        x.append(xt); y.append(yt);

    x_set = list(set(x)); y_set = list(set(y));
    print(2*sum(x_set)-sum(x),2*sum(y_set)-sum(y))
