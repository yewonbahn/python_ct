def solution(s):
    answer = True
    pcnt=s.count("p")+s.count("P")
    ycnt=s.count("y")+s.count("Y")
    if pcnt!=ycnt:
        return False

    return True