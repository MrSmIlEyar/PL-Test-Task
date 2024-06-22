import sys

args = sys.argv
n, m = int(args[1]), int(args[2]) - 1
mas = list(range(1, n + 1))
result = []
k = 0
while k != 0 or len(result) == 0:
    result.append(str(mas[k]))
    if k + m >= n:
        k = m - (n - k)
    else:
        k += m
print(''.join(result))
