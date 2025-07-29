# 스택 수열
n = int(input())
stack = []
i = 1
answer = []
for _ in range(n):
    num = int(input())
    while i <= num:
        stack.append(i)
        i += 1
        answer.append("+")
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    
if len(stack) >= 1:
    print("NO")
else:
    for i in answer:
        print(i)