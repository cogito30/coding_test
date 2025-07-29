# [PCCP 기출문제] 1번 / 동영상 재생기
def check_opening(pos_mm, pos_ss, op_start_time, op_end_time):
    current_time = pos_mm * 100 + pos_ss
    if op_start_time <= current_time and current_time <= op_end_time:
        current_time = op_end_time
    pos_mm = current_time // 100
    pos_ss = current_time % 100
    return pos_mm, pos_ss

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len_mm = int(video_len[:2])
    video_len_ss = int(video_len[3:])
    pos_mm = int(pos[:2])
    pos_ss = int(pos[3:])
    op_start_time = int(op_start[:2] + op_start[3:])
    op_end_time = int(op_end[:2] + op_end[3:])
    
    for command in commands:
        pos_mm, pos_ss = check_opening(pos_mm, pos_ss, op_start_time, op_end_time)
        
        if command == "prev":
            pos_ss -= 10
            if pos_ss < 0:
                pos_ss += 60
                pos_mm -= 1
            if pos_mm < 0:
                pos_mm = 0
                pos_ss = 0
        elif command == "next":
            pos_ss += 10
            if pos_ss > 60:
                pos_ss -= 60
                pos_mm += 1
            if pos_mm == video_len_mm and pos_ss > video_len_ss:
                pos_ss = video_len_ss
            if pos_mm > video_len_mm:
                pos_mm = video_len_mm
                pos_ss = video_len_ss
    
        pos_mm, pos_ss = check_opening(pos_mm, pos_ss, op_start_time, op_end_time)
    
    if pos_mm < 10:
        answer += "0"
    answer += str(pos_mm)
    answer += ":"
    if pos_ss < 10:
        answer += "0"
    answer += str(pos_ss)
    
    return answer