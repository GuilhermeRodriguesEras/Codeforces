import math

values = list(map(int, input().split()))
n, m, a = values[0],  values[1], values[2]

necessaryFlagstones  = math.ceil(n/a) * math.ceil(m/a)

print(necessaryFlagstones)