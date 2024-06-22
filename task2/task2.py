import sys

args = sys.argv
circle_file = open(args[1], "r")
center_x, center_y = list(map(int, circle_file.readline().strip().split()))
radius = int(circle_file.readline().strip())
circle_file.close()
dots_file = open(args[2], "r")
dots = [list(map(int, dot.strip().split())) for dot in dots_file.readlines()]
dots_file.close()
radius_pow = radius ** 2

for dot in dots:
    s1 = (dot[0] - center_x) ** 2
    s2 = (dot[1] - center_y) ** 2
    if s1 + s2 > radius_pow:
        print(2)
    elif s1 + s2 == radius_pow:
        print(0)
    else:
        print(1)
