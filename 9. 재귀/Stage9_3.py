import sys


def star_10(n):
    if n == 1:
        return ['*']

    stars = star_10(n // 3)
    star_line = list()

    for star in stars:
        star_line.append(star * 3)

    for star in stars:
        star_line.append(star + ' ' * (n // 3) + star)

    for star in stars:
        star_line.append(star * 3)

    return star_line


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    star = star_10(N)
    print('\n'.join(star))
