import sys

if __name__ == '__main__':
    a = input().split(' ')
    word_cnt = len(a)

    if not a[0]:
        word_cnt -= 1

    if not a[-1]:
        word_cnt -= 1

    print(word_cnt)
