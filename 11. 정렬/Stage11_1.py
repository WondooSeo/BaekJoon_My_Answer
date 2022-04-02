import sys

if __name__ == '__main__':
    N = int(input())
    num_list = []

    for _ in range(N):
        num = int(input())
        num_list.append(num)

    # Long live 'sorted()' !!!

    # Insert sort
    # for i in range(1,len(num_list)):
    #     for j in range(i,0,-1):
    #         if num_list[j-1] > num_list[j]:
    #             num_list[j-1], num_list[j] = num_list[j], num_list[j-1]

    # for num in num_list:
    #     print(num)

    # Bubble sort
    for i in range(len(num_list)-1,0,-1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j],num_list[j+1] = num_list[j+1],num_list[j]

    for num in num_list:
        print(num)
