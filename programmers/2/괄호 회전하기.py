def solution(s):
    def check(string):
        lst = []
        for i in string:
            if (i == "]" or i == "}" or i == ")") and len(lst) == 0:
                lst.append(i)
            if i == "]" and len(lst) != 0:
                if lst[-1] == "[":
                    lst.pop()
            if i == "}" and len(lst) != 0:
                if lst[-1] == "{":
                    lst.pop()
            if i == ")" and len(lst) != 0:
                if lst[-1] == "(":
                    lst.pop()
            if i == "(" or i == "{" or i == "[":
                lst.append(i)

        if len(lst) == 0:
            return True
        else:
            return False
    error = 0
    ori = s
    for j in range(len(s)):
        if check(ori):
            error += 1
        ori = ori[1:len(ori)] + ori[0]
    return error