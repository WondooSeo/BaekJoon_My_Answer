import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    
    for _ in range(N):
        cloth_case = int(sys.stdin.readline().rstrip())
        cloth_dict = dict()

        for _ in range(cloth_case):
            _, cloth_type = sys.stdin.readline().rstrip().split()
            if cloth_type not in cloth_dict:
                cloth_dict[cloth_type] = 1
            else:
                cloth_dict[cloth_type] += 1

        count = 1
        for key in list(cloth_dict.keys()):
            count *= (cloth_dict[key]+1)

        print(count-1)
