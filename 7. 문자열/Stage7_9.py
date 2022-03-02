import sys

if __name__ == '__main__':
    word = list(sys.stdin.readline().rstrip())
    len_word = len(word)
    count = 0
    pivot = 0
    while pivot < len_word:
        if word[pivot] == 'c' and pivot+1<len_word and (word[pivot+1]=='=' or word[pivot+1]=='-'):
                count += 1
                pivot += 2
        elif word[pivot] == 'd' and pivot+2<len_word and word[pivot+1]=='z' and word[pivot+2]=='=':
                count += 1
                pivot += 3
        elif word[pivot] == 'd' and pivot+1<len_word and word[pivot+1]=='-':
                count += 1
                pivot += 2
        elif word[pivot] == 'l' and pivot+1<len_word and word[pivot+1]=='j':
                count += 1
                pivot += 2
        elif word[pivot] == 'n' and pivot+1<len_word and word[pivot+1]=='j':
                count += 1
                pivot += 2
        elif word[pivot] == 's' and pivot+1<len_word and word[pivot+1]=='=':
                count += 1
                pivot += 2
        elif word[pivot] == 'z' and pivot+1<len_word and word[pivot+1]=='=':
                count += 1
                pivot += 2
        else:
            count += 1
            pivot += 1

    print(count)

# Another explanation
'''
import sys

if __name__ == '__main__':
    word = list(sys.stdin.readline().rstrip())
    croat_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for croat_ch in croat_list:
        word = word.replace(croat_ch,'*')

    print(len(word))
'''
