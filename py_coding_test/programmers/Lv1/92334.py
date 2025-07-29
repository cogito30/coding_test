# 신고 결과 받기
def solution(id_list, report, k):
    answer = []
    user_other = {}
    other_user = {}
    ban_list = []
    for i in id_list:
        user_other[i] = set()
        other_user[i] = set()
        
    for r in report:
        user, other = r.split()
        user_other[user].add(other)
        other_user[other].add(user)
        
    for i in id_list:
        if len(other_user[i]) >= k:
            ban_list.append(i)
    
    for i in id_list:
        count = 0
        for j in user_other[i]:
            if j in ban_list:
                count += 1
        answer.append(count)
        
    return answer