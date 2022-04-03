import sys

if __name__ == '__main__':
    a = input().upper()
    a_list = list(set(a))

    cnt = []
    for c in a_list:
        cnt.append(a.count(c))

    if cnt.count(max(cnt)) > 1:
        print('?')
    else:
        print(a_list[cnt.index(max(cnt))])
