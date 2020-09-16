from gcd import gcd


# Least Common Multiplier
def lcm(a, b):
    return a * b / gcd(a, b)
