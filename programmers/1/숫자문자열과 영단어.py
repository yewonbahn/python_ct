def solution(s):
    answer=''
    p_dict={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    reverse_dict= dict(map(reversed,p_dict.items()))
    word=''
    for i in range(len(s)):
        if s[i].isdigit():
            answer+=s[i]
            continue
        word+=s[i]
        if word in reverse_dict.keys():
            answer+=str(reverse_dict[word])
            word=''

    return int(answer)
