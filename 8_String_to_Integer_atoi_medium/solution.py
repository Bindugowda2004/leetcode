##Input Parsing, Expressions, Libraries.

#Manual Parsing (atoi_manual.py)

def myAtoi(s):
    s = s.strip()
    if not s: return 0
    sign, i = 1, 0
    if s[0] in "+-":
        sign = -1 if s[0] == "-" else 1
        i += 1
    res = 0
    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1
    res *= sign
    return min(max(res, -2**31), 2**31 - 1)


#Regex Approach (atoi_regex.py)

import re
def myAtoi(s):
    match = re.match(r'^[\+\-]?\d+', s.strip())
    if not match: return 0
    res = int(match.group())
    return min(max(res, -2**31), 2**31 - 1)