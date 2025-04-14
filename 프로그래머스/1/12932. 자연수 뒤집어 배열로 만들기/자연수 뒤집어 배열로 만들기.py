def solution(n):
    answer = []
    new_list=list(map(int,str(n)))
    for i in new_list:
        answer.append(i)
    return answer[::-1]