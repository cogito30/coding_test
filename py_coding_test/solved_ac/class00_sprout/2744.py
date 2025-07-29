# 대소문자 바꾸기
word = input()

for ch in word:
    if ch.isupper():
        print(ch.lower(), end="")
    elif ch.islower():
        print(ch.upper(), end="")