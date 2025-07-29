# [카카오 인턴] 키패드 누르기
def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7, -2] # -2는 "*"
    right = [3, 6, 9, -1] # -1은 "#"
    middle = [2, 5, 8, 0]
    
    left_hand = (3, 0) 
    right_hand = (3, 2)
    for i in numbers:
        if i in left:
            answer += "L"
            left_hand = (left.index(i), 0)
        elif i in right:
            answer += "R"
            right_hand = (right.index(i), 2)
        elif i in middle:
            middle_pos = (middle.index(i), 1)
            diff_left = abs(left_hand[0] - middle_pos[0]) + abs(left_hand[1] - middle_pos[1])
            diff_right = abs(right_hand[0] - middle_pos[0]) + abs(right_hand[1] - middle_pos[1])
            if diff_left == diff_right:
                if hand == "right":
                    answer += "R"
                    right_hand = (middle_pos[0], middle_pos[1])
                elif hand == "left":
                    answer += "L"
                    left_hand = (middle_pos[0], middle_pos[1])
            elif diff_left > diff_right:
                answer += "R"
                right_hand = (middle_pos[0], middle_pos[1])
            elif diff_left < diff_right:
                answer += "L"
                left_hand = (middle_pos[0], middle_pos[1])
            
                    
            
    
    return answer