# 대소문자 바꾸서 출력하기
str = input()
answer = ""
for i in str:
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)