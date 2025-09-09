#Greedy Approach

def intToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res = ""
    for i in range(len(val)):
        while num >= val[i]:
            res += syms[i]
            num -= val[i]
    return res


#Mapping Dictionary Approach

def intToRoman(num):
    mapping = {1000:"M",900:"CM",500:"D",400:"CD",
               100:"C",90:"XC",50:"L",40:"XL",
               10:"X",9:"IX",5:"V",4:"IV",1:"I"}
    res = ""
    for val, sym in mapping.items():
        while num >= val:
            res += sym
            num -= val
    return res