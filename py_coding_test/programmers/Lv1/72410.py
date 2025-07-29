# 신규 아이디 추천
def solution(new_id):
    answer = ''
    first = ''
    # 1,2단계
    for i in new_id:
        if i.isupper():
            first += i.lower()
        elif i.islower() or i.isdecimal() or i == "-" or i == "_" or i ==".":
            first += i
    
    # 3단계
    third = first[0]
    for i in range(1, len(first)):
        if first[i] == "." and first[i] == first[i-1]:
            continue
        else:
            third += first[i]
    
    fourth = third.strip(".")
    
    fifth = fourth
    if len(fourth) == 0:
        fifth += "a"
    
    sixth = fifth
    if len(sixth) >= 16:
        sixth = fifth[:15]
        if sixth[-1] == ".":
            sixth = sixth[:-1]
    print(sixth)
    seven = sixth
    if len(seven) <= 2:
        seven += sixth[-1] * (3-len(seven))
    
    answer = seven
    return answer