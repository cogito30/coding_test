# FizzBuzz
A = input()
B = input()
C = input()

answer = 0
if C.isnumeric():
    answer = int(C) + 1
elif B.isnumeric():
    answer = int(B) + 2
elif A.isnumeric():
    answer = int(A) + 3

if answer % 3 == 0 and answer % 5 == 0:
    print("FizzBuzz")
elif answer % 3 == 0:
    print("Fizz")
elif answer % 5 == 0:
    print("Buzz")
else:
    print(answer)