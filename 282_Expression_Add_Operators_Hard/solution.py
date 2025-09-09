#approach 1 : DFS Backtracking (dfs_backtracking.py)

def addOperators(num, target):
    res = []
    def dfs(path, pos, value, prev):
        if pos == len(num):
            if value == target:
                res.append(path)
            return
        for i in range(pos+1, len(num)+1):
            cur_str, cur_val = num[pos:i], int(num[pos:i])
            if len(cur_str) > 1 and cur_str[0] == "0":
                break
            if pos == 0:
                dfs(cur_str, i, cur_val, cur_val)
            else:
                dfs(path+"+"+cur_str, i, value+cur_val, cur_val)
                dfs(path+"-"+cur_str, i, value-cur_val, -cur_val)
                dfs(path+"*"+cur_str, i, value-prev+prev*cur_val, prev*cur_val)
    dfs("", 0, 0, 0)
    return res


#approach 2 : Using eval with generation (eval_expression.py)

def addOperators(num, target):
    res = []
    def dfs(path, pos):
        if pos == len(num):
            if eval(path) == target:
                res.append(path)
            return
        for i in range(pos+1, len(num)+1):
            cur = num[pos:i]
            if len(cur) > 1 and cur[0] == "0":
                break
            if pos == 0:
                dfs(cur, i)
            else:
                for op in "+-*":
                    dfs(path+op+cur, i)
    dfs("", 0)
    return res