# 잃어버린 괄호
expression = input()
total_num = 0
sign = 1
num = "0"
for i in expression:
    if i in "0123456789":
        num += i
    elif i == "+":
        total_num += int(num) * sign
        num = "0"   
    elif i == "-":
        total_num += int(num) * sign
        sign = -1
        num = "0"

if num != "0":
    total_num += int(num) * sign

print(total_num)