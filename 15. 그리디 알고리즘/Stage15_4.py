### First try:
# import sys

# def calc_calc(list_str_num, sign):
#     if sign == '+':
#         return int(''.join(list_str_num))
#     else:
#         return -int(''.join(list_str_num))


# if __name__ == '__main__':
#     calc = list(sys.stdin.readline().rstrip())
#     now_num = list(); calc_result = 0; now_sign = '+'

#     for calc_chr in calc:
#         if calc_chr == '-':
#             calc_result += calc_calc(now_num, now_sign)
#             now_sign = '-'; now_num = list();

#         elif calc_chr == '+':
#             calc_result += calc_calc(now_num, now_sign)
#             now_num = list()

#         else:
#             now_num.append(calc_chr)

#     calc_result += calc_calc(now_num, now_sign)
#     print(calc_result)


### Modified try:
import sys

if __name__ == '__main__':
    calc = sys.stdin.readline().rstrip().split('-')
    now_result = 0

    now_result += sum(list(map(int,calc[0].split('+'))))

    if len(calc) > 1:
        for i in range(1,len(calc)):
            now_result -= sum(list(map(int,calc[i].split('+'))))

    print(now_result)
