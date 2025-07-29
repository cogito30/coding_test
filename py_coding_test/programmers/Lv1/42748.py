# K번째수
def solution(array, commands):
    answer = []
    for command in commands:
        sliceArray = array[command[0]-1:command[1]]
        sliceArray.sort()
        answer.append(sliceArray[command[2]-1])

    return answer