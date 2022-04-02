import sys

def gcd(a,b):
    while a > 0:
        b = b%a
        a,b = b,a

    return b


if __name__ == '__main__':

    N = int(sys.stdin.readline().rstrip())
    
    num_list = list()

    for i in range(N):
        num_list.append(int(sys.stdin.readline().rstrip()))
        if i == 0:
            continue
        elif i == 1:
            now_gcd = abs(num_list[i]-num_list[i-1])
        else:
            now_gcd = gcd(now_gcd,abs(num_list[i]-num_list[i-1]))

    yaksu = list()

    for i in range(2,int(now_gcd**0.5)+1):
        if now_gcd%i == 0:
            yaksu.append(i)
            yaksu.append(now_gcd//i)

    yaksu.append(now_gcd)
    print(*sorted(set(yaksu)))
