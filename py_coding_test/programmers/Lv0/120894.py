# 영어가 싫어요
def solution(numbers):
    answer = ""
    word = ""
    word_to_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(numbers)):
        word += numbers[i]
        if word in word_to_num:
            answer += str(word_to_num.index(word))
            word = ""
    answer = int(answer)
    return answer