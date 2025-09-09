#Basic Calculator (LeetCode 224)

##Expression evaluation, stack, libraries.

#Stack Approach

def calculate(s):
    stack, res, num, sign = [], 0, 0, 1
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in "+-":
            res += sign * num
            num = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1
        elif ch == ")":
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + sign * num