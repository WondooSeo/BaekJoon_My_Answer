import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    word_list = []

    for _ in range(n):
        word_list.append(sys.stdin.readline().rstrip())

    word_list = list(set(word_list))
    sorted_word_list = sorted(word_list, key=lambda x: (len(x), x))

    for word in sorted_word_list:
        print(word)
