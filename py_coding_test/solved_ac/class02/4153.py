# 직각삼각형
while True:
    sides = list(map(int, input().split()))
    if sides[0] == 0 and sides[1] == 0 and sides[2] == 0:
        break
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("right")
    else:
        print("wrong")

"""
while True:
    length = [int(i) for i in input().split()]
    if sum(length) == 0:
        break
    length.sort()
    if (length[2] ** 2) == ((length[0] ** 2) + (length[1] ** 2)):
        print("right")
    else:
        print("wrong")
"""