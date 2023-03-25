import math

#最大公約数
n, m = map(int, input().split())
print(math.gcd(n,m))

#最小公倍数
def lcm(h, w):
    return int(h * w / math.gcd(h, w))
print(lcm(n,m))