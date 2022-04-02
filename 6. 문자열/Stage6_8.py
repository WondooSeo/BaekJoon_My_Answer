import sys

if __name__ == '__main__':
    word = sys.stdin.readline().rstrip()
    dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    word_list = list(word.upper())
    count = 0

    for i in word_list:
        for j in range(len(dial)):
            if i in dial[j]:
                count += (j + 3)
                break

    print(count)
