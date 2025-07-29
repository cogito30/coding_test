# 알파벳 찾기
s = input()
answer = [-1 for _ in range(26)]
# 중복 문자 주의
for i in range(len(s)):
    if answer[ord(s[i])-ord('a')] == -1:
        answer[ord(s[i])-ord('a')] = i
for i in answer:
    print(i, end=" ")

"""
s = input()
answer = [-1 for _ in range(26)]
for i in s:
    answer[ord(i) - ord('a')] = s.find(i)
for i in answer:
    print(i, end=" ")
"""