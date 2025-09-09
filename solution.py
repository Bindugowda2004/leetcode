##1
#Math Approach (reverse_integer_math)

def reverse(x):
    res, sign = 0, 1 if x >= 0 else -1
    x = abs(x)
    while x:
        res = res * 10 + x % 10
        x //= 10
    return 0 if res > 2**31 - 1 else res * sign

##2
#String Approach (reverse_integer_string)

def reverse(x):
    s = str(abs(x))[::-1]
    res = int(s)
    if res > 2**31 - 1:
        return 0
    return res if x >= 0 else -res